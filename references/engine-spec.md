# 引擎规格（改引擎前必读）

> 对应的实现文件：`assets/deck-shell.html`。改内容不用读本文；要改引擎行为、调参、排障时读。

---

## 一、四层结构

```
① 舞台层   #viewport + #deck(1600×900) + fit() 等比 scale
② 版式层   .slide / .slide.dark ＋ 每种版式一套 grid
③ 动效层   rise / drift / zoom / fade / stagger / emphasis ＋ 主时钟同步
④ 控制层   时间轴 / 暂停 / 自动演示 / 讲稿 / 打印 / 键盘
```

### 舞台层

```css
#deck{position:absolute;left:50%;top:50%;margin-left:-800px;margin-top:-450px;
      width:1600px;height:900px;transform-origin:center center}
```
```js
function fit(){
  const s = Math.min(viewport.clientWidth/1600, viewport.clientHeight/900);
  deckEl.style.transform = 'scale(' + s + ')';
}
```

版式一律按 1600×900 的像素写死，**不做响应式重排**。所有屏幕只缩放不换版，投影、笔记本、预览三处构图一致。这是整套方案能稳定复现的前提，不要改成 `vw/vh` 或 flex 流式布局。

---

## 二、主时钟：整套方案的核心

**原理**：每个元素的动画创建后立即 `pause()`，再由一个隐藏元素的空动画充当时间源，每帧把所有子动画的 `currentTime` 写成主时钟的时间。

```js
function anim(el, frames, delay, dur, easing){
  el.classList.add('motion-unit');
  const a = el.animate(frames, {delay, duration:dur, fill:'both', iterations:1, easing});
  a.pause();                    // ← 关键
  a.currentTime = 0;
  effects.push(a);
  return a;
}

driver = clockEl.animate([{opacity:0},{opacity:0}], {duration:len, fill:'both'});
driver.pause();

function sync(){
  const t = Math.min(duration, driver.currentTime);
  effects.forEach(a => a.currentTime = t);       // ← 全部跟随
  slide.style.setProperty('--motion-progress', t/duration);
}
```

**为什么不能让动画自己播**：

| 自播 | 主时钟驱动 |
|---|---|
| 无法暂停在某一帧 | 暂停即冻结全部 |
| 无法拖进度条回看 | 拖动 = 改 `driver.currentTime` |
| 重播要逐条重建 | 重置主时钟即可 |
| 换页残留动画无法清理 | `effects.forEach(cancel)` 一次清空 |

**改动约束**：任何新增的入场/强调都必须走 `anim()`，不要直接 `el.animate(...).play()`，否则该元素会脱离时间轴。

---

## 三、原语与参数基线

| 原语 | 实现 | 默认参数 |
|---|---|---|
| `rise` | `opacity 0→1` + `translate3d(dx,dy,0)` → `none` | dy=22，dx=0，dur=650 |
| `drift` | 同上，横向 | dx=-26，dy=0，dur=700 |
| `zoom` | `opacity 0→1` + `scale(s-0.02)` → `scale(s)` | s=1.035，dur=1600 |
| `fade` | 仅透明度 | dur=650 |
| `stagger` | 对父容器子元素批量 `rise` | base=600，gap=180 |
| `emphasis` | 底色 0→8%→8%→0，同步左侧 3px 竖线 | 起点 2200，dur=1200 |

| 参数 | 取值 | 理由 |
|---|---|---|
| 入场位移 | ≤ 26 px | 再大就像"飞入"，失去专业感 |
| 入场时长 | 550–850 ms | 短于 500 显仓促，长于 900 显拖沓 |
| 缓动 | `cubic-bezier(.2,.75,.25,1)` | 前快后慢，落位感 |
| 强调缓动 | `cubic-bezier(.4,0,.2,1)` | 进出对称，不刺眼 |
| 交错间隔 | 170–250 ms | <150 糊成一片，>300 节奏断裂 |
| 强调时长 | 1200–1800 ms | 三段：进 18% / 停 / 退 |
| 单页时长 | 8000 ms | 超过 10 s 观众开始等结尾 |
| 画布 | 1600×900 | 16:9，与投影 1:1 |
| 内容内边距 | 68 / 86 px | 有效画布 1428×764 |

**强调的配色**：浅色页 8% 主色底，深色页 12–13% 辅助色底；竖线固定 `inset 3px 0 0 var(--accent)`。

**表格行强调**：`<tr>` 不渲染 `box-shadow`，代码里已自动把竖线改画到 `el.cells[0]`，不要改回去。

---

## 四、时间预算

单页时长由 `data-hold` 决定（默认 8000 ms）。生成内容时必须自检：

```
末条强调起点 + 强调时长 + 400ms  ≤  data-hold
```

不满足就会"强调还没走完就换页"。6 行的表格页建议 `data-hold="8600"`。

---

## 五、控制层行为

| 键 | 作用 |
|---|---|
| `← →` / 空格 / PgUp PgDn | 翻页 |
| `Home` / `End` | 首尾页 |
| `R` | 重播当前页动效 |
| `P` | 暂停 / 播放页内动效 |
| `M` | 动效开 / 关（关闭后全部元素直接可见） |
| `A` | 自动演示（配合 20/25/35 秒停留） |
| `N` | 讲稿抽屉 |
| `F` | 全屏 |
| `Esc` | 退出全屏 / 关讲稿 |

**外部接口**（自动化截图、录制、二次开发）：

```js
window.motionDeck = {
  goto(i), seek(ms), play(), pause(), replay(),
  setEnabled(bool), setAuto(bool), setHold(sec), setPalette('teal'|'blue'|'graphite'),
  getState()   // {slide,totalSlides,currentTime,duration,enabled,playing,autoMode,effectCount,holdSeconds,palette}
}
window.deckState = {index, total, title}
```

---

## 六、打印与 PDF

两层保障，缺一不可：

1. `beforeprint` 把主时钟推到 `duration`，打印完 `afterprint` 还原；
2. `@media print` 里 `.motion-unit{opacity:1!important;transform:none!important}`。

```css
@media print{
  @page{size:1600px 900px;margin:0}
  .slide,.slide.active{display:block!important;width:1600px;height:900px;
                       break-after:page;print-color-adjust:exact}
}
```

验证方法：`scripts/validate_deck.py --pdf out.pdf` 会数页数，必须等于 section 数。

---

## 七、配色令牌

全部色值集中在 `body{--...}`，共 16 个变量：

```
--paper --ink --muted --accent --accent-soft --line --table-head
--dark --dark-ink --dark-muted --stage --cover --cover-ink --cover-sub
--emph --emph-dark
```

内置三套：`data-palette="teal"`（医院青）/ `"blue"`（工程蓝）/ `"graphite"`（石墨灰）。
新增一套只需复制一个 `body[data-palette="xxx"]{...}` 块，不需要动任何布局规则。

**注意**：`emphasis()` 会运行时读 `--emph` / `--emph-dark` / `--accent`，因此换配色后强调色自动跟随；如果新增变量名，记得同步改 `emphasis()` 里的 `cssVar()` 调用。

---

## 八、坑

| 现象 | 原因 | 处理 |
|---|---|---|
| PDF 空白页 | 元素停在 `opacity:0` | `beforeprint` 推末帧 + print 里的 `!important` 规则 |
| 表格行只有底色没有竖线 | `<tr>` 不渲染 `box-shadow` | 已自动改画到 `cells[0]` |
| 换页后旧动画残留 | 未取消上一页动画 | `stop()` 里 `effects.forEach(cancel)` |
| 第二次进同一页不播 | 主时钟已结束 | `build()` 重建 |
| 单文件 8 MB 打不开 | 内嵌原图 | 图片压到宽 ≤1000 px、质量 80 再 base64 |
| 深色页文字看不清 | 只改底色没改字色 | 用 `.dark` 类，成对覆盖前景色 |
| 投影边缘被裁 | 装饰元素超出画布 | 所有装饰限制在 1600×900 内 |
| 打印多出空白页 | 页面高度不是精确 900 | `@page` 尺寸必须与 `#deck` 完全一致 |

---

## 九、改引擎的自检

改完 `deck-shell.html` 后必须跑：

```bash
python scripts/validate_deck.py assets/example-deck.html --pdf /tmp/check.pdf
```

再跑一次 `references/layouts.md` 的 13 页合成稿，确认所有版式都没被改坏。
