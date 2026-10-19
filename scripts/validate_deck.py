#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_deck.py —— 动效演示文稿交付前自检

用法：
    python validate_deck.py <deck.html>
    python validate_deck.py deck.html --shots ./shots --pdf deck.pdf
    python validate_deck.py deck.html --json

检查项：
    1. section 数量 == deck-data 条数
    2. 逐页激活并推到末帧：控制台报错 / 页面异常
    3. 版面溢出：正文流元素越过脚注区，或右侧越界
    4. 正文流与 bottom-note 重叠
    5. 打印页数 == 页数（验证 @media print 与 beforeprint 冻结末帧）

依赖：playwright（本机已有 Chrome 即可，用 channel="chrome"）
退出码：0 全部通过；1 存在阻断性问题。
"""
import argparse
import json
import pathlib
import re
import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("缺少 playwright：pip install playwright（无需 playwright install，本机 Chrome 即可）")

# 页面底部的脚注安全带：正文流不得进入 slide 底部 100px
BOTTOM_SAFE = 100
RIGHT_SAFE = 20


def load_browser(p):
    """优先用本机 Chrome，失败再退 Edge / 内置 Chromium。"""
    for kwargs in ({"channel": "chrome"}, {"channel": "msedge"}, {}):
        try:
            return p.chromium.launch(headless=True, **kwargs)
        except Exception:
            continue
    raise RuntimeError("找不到可用浏览器：请安装 Chrome 或执行 playwright install chromium")


MEASURE_JS = """
(i) => {
  const s = document.querySelectorAll('.slide')[i];
  const box = s.getBoundingClientRect();
  const note = s.querySelector('.bottom-note');
  const noteTop = note ? note.getBoundingClientRect().top : null;

  let flowBottom = -1e9, rightMax = -1e9, worst = '';
  s.querySelectorAll('*').forEach(el => {
    const cs = getComputedStyle(el);
    if (cs.position === 'absolute' || cs.position === 'fixed') return;
    const r = el.getBoundingClientRect();
    if (!r.height || !r.width) return;
    if (r.bottom > flowBottom) { flowBottom = r.bottom; worst = el.tagName + '.' + (el.className || ''); }
    if (r.right > rightMax) rightMax = r.right;
  });

  return {
    slide: i + 1,
    flowBottom: Math.round(flowBottom),
    noteTop: noteTop === null ? null : Math.round(noteTop),
    rightMax: Math.round(rightMax),
    boxBottom: Math.round(box.bottom),
    boxRight: Math.round(box.right),
    worst
  };
}
"""


def main():
    ap = argparse.ArgumentParser(description="动效演示文稿自检")
    ap.add_argument("html", help="待检查的 html 文件")
    ap.add_argument("--shots", help="逐页截图输出目录（末帧）")
    ap.add_argument("--pdf", help="导出 PDF 到该路径，并校验页数")
    ap.add_argument("--width", type=int, default=1600)
    ap.add_argument("--height", type=int, default=900)
    ap.add_argument("--json", action="store_true", help="只输出 JSON 结果")
    args = ap.parse_args()

    path = pathlib.Path(args.html).resolve()
    if not path.exists():
        sys.exit(f"文件不存在：{path}")

    shots = pathlib.Path(args.shots).resolve() if args.shots else None
    if shots:
        shots.mkdir(parents=True, exist_ok=True)

    problems, warnings = [], []
    result = {"file": str(path), "slides": 0, "pages": None, "issues": [], "warnings": []}

    with sync_playwright() as p:
        browser = load_browser(p)
        page = browser.new_page(
            viewport={"width": args.width, "height": args.height + 106}  # 106 = 控制条 58 + 动效条 48
        )
        errs = []
        page.on("pageerror", lambda e: errs.append("PAGEERROR " + str(e)))
        page.on("console", lambda m: errs.append("CONSOLE " + m.text) if m.type == "error" else None)
        page.goto(path.as_uri())
        page.wait_for_timeout(600)

        n = page.evaluate("document.querySelectorAll('.slide').length")
        result["slides"] = n
        if n == 0:
            sys.exit("未找到 .slide，页面结构不对")

        # 1. deck-data 条数
        try:
            data_len = page.evaluate(
                "JSON.parse(document.getElementById('deck-data').textContent).length"
            )
        except Exception as e:
            data_len = -1
            problems.append(f"deck-data 解析失败：{e}")
        if data_len != n:
            problems.append(f"deck-data 条数({data_len}) != section 数({n})，讲稿抽屉会错位")

        # 2~4. 逐页激活测量
        has_api = page.evaluate("typeof window.motionDeck === 'object'")
        if not has_api:
            warnings.append("未找到 window.motionDeck，改用点击翻页（无末帧定位）")

        for i in range(n):
            if has_api:
                page.evaluate(f"window.motionDeck.goto({i})")
                page.wait_for_timeout(80)
                page.evaluate("window.motionDeck.seek(window.motionState.duration)")
            else:
                page.evaluate(f"location.hash = '#{i + 1}'")
            page.wait_for_timeout(90)

            m = page.evaluate(MEASURE_JS, i)
            if m["flowBottom"] > m["boxBottom"] - BOTTOM_SAFE:
                problems.append(
                    f"第{m['slide']}页底部溢出：正文到 {m['flowBottom']}px，"
                    f"安全线 {m['boxBottom'] - BOTTOM_SAFE}px（末元素 {m['worst']}）"
                )
            if m["noteTop"] is not None and m["flowBottom"] > m["noteTop"] - 8:
                problems.append(
                    f"第{m['slide']}页正文压到脚注：正文 {m['flowBottom']}px > 脚注顶 {m['noteTop']}px"
                )
            if m["rightMax"] > m["boxRight"] - RIGHT_SAFE:
                problems.append(f"第{m['slide']}页右侧越界：{m['rightMax']}px > {m['boxRight'] - RIGHT_SAFE}px")

            if shots:
                page.locator("#deck").screenshot(path=str(shots / f"slide{i + 1:02d}.png"))

        # 5. 打印页数
        if args.pdf:
            pdf_path = pathlib.Path(args.pdf).resolve()
            pdf_path.parent.mkdir(parents=True, exist_ok=True)
            page.pdf(
                path=str(pdf_path),
                width=f"{args.width}px",
                height=f"{args.height}px",
                print_background=True,
                margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            )
            raw = pdf_path.read_bytes()
            pages = len(re.findall(rb"/Type\s*/Page[^s]", raw))
            result["pages"] = pages
            if pages != n:
                problems.append(f"打印页数 {pages} != 页数 {n}（检查 @media print 与 beforeprint）")

        if errs:
            for e in errs[:10]:
                problems.append(e)

        browser.close()

    result["issues"] = problems
    result["warnings"] = warnings
    result["ok"] = not problems

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=1))
    else:
        print(f"文件：{path.name}")
        print(f"页数：{result['slides']}" + (f"　打印：{result['pages']} 页" if result["pages"] else ""))
        if warnings:
            for w in warnings:
                print(f"  [提示] {w}")
        if problems:
            print(f"\n发现 {len(problems)} 个问题：")
            for pr in problems:
                print(f"  ✗ {pr}")
        else:
            print("\n全部通过：条数一致、无报错、无溢出、无遮挡" + ("、打印页数正确" if result["pages"] else ""))

    sys.exit(0 if not problems else 1)


if __name__ == "__main__":
    main()
