# 版式库（13 种）

> 全部片段可直接粘进 `assets/deck-shell.html` 的 `SLIDES` 标记处。
> 类名与 `deck-shell.html` 里的 CSS 一一对应，不要改名。
> 动效只靠 `data-*` 属性声明，不需要改引擎。

---

## 选用速查

| # | 版式 | 选择器 | 适合承载 | 条数上限 | 强调目标 |
|---|---|---|---|---|---|
| 1 | 封面 | `.cover` | 标题 + 副题 + 身份 | 副题 2 行 | 无 |
| 2 | 问题页 | `.problem-layout` | 左一句判断 + 右三条 | 3 条 | 无 |
| 3 | 价值行 | `.value-rows` | 四类对象各一行 | 3–5 行 | 逐行 |
| 4 | 依据行 | `.source-rows` | 数据/材料来源 | 2–4 行 | 逐行 |
| 5 | 四宫格 | `.rigor-grid` | 四条原则、两层对照 | 4 块（2×2） | 小标题 |
| 6 | 表格 | `table.hardware` | 参数、设备、对照 | 4–6 行 × 3 列 | 逐行 |
| 7 | 四步流程 | `.ai-flow` | 方法步骤、建设路径 | 4 步 | 逐栏 |
| 8 | 三栏阶段 | `.vision-line` | 三阶段路线 | 3 栏 | 逐栏 |
| 9 | 左标题右条 | `.wearable-layout` | 一句主张 + 三条场景 | 3 条 | 逐条 |
| 10 | 左标题右块 | `.vr-layout` | 一句主张 + 三问 | 3 块 | 逐块 |
| 11 | 图 + 文 | `.space-layout` | 截图、模型、照片 | 1 图 | 结论句 |
| 12 | 两栏备查 | `.reference-layout` | 资料、参考文献 | 2 栏 | 无 |
| 13 | 收尾 | `.value-close` | 三行结论 + 致谢 | 3 行 | 无 |

**容量红线**：正文超过 2 行（约 30 字/行）就换版式，不要缩字号。

---

## 1. 封面

```html
<section class="slide cover" id="slide-1" aria-label="1 标题">
  <div class="cover-copy">
    <p class="occasion" data-anim="rise" data-at="0" data-dur="600" data-dy="12">2026年XX大赛 XX方向</p>
    <h1>
      <strong data-anim="rise" data-at="180" data-dur="850" data-dy="34">主标题四到六字</strong>
      <span data-anim="rise" data-at="550" data-dur="700" data-dy="18">副题第一行</span>
      <span data-anim="rise" data-at="730" data-dur="700" data-dy="18">副题第二行</span>
    </h1>
    <p class="cover-sub" data-anim="rise" data-at="1050" data-dur="750">一句话价值主张</p>
    <p class="identity" data-anim="rise" data-at="1370" data-dur="650">参赛单位：XX<br>汇报人：XX</p>
  </div>

  <!-- 右侧图示卡：可整块删掉，删后标题区宽度改为 1200px -->
  <div class="cover-card" data-anim="zoom" data-at="100" data-dur="1600" data-scale="1.035">
    <h3>右侧小标题</h3>
    <div class="row"><b>标签一<i>0 – 1.0 s</i></b><div class="track"><i style="left:0;width:12.5%"></i></div></div>
    <div class="row"><b>标签二<i>0.6 – 3.2 s</i></b><div class="track"><i style="left:7.5%;width:32.5%"></i></div></div>
    <p class="cap">图注一句话。</p>
  </div>

  <span class="page-number">01 / 13</span>
  <div class="tmpl-brand">单位 · 项目名</div>
</section>
```

---

## 2. 问题页（左判断 + 右三条）

```html
<section class="slide paper" id="slide-2" aria-label="2 标题">
  <h2 data-anim="rise" data-at="0" data-dur="600" data-dx="-18" data-dy="0">标题：一个判断句，不超过 26 字</h2>

  <div class="problem-layout">
    <div class="lead-block" data-anim="rise" data-at="500" data-dur="850">
      <p class="big-line">左侧大字，<br>三到四行内说完。</p>
      <p>补一句解释，<br>说明为什么重要。</p>
    </div>

    <div class="item-list" data-stagger="700" data-gap="200">
      <div class="item"><span class="ordinal">01</span>
        <div><h3>小标题</h3><p>一句半到两句，不超过 30 字。</p></div></div>
      <div class="item"><span class="ordinal">02</span>
        <div><h3>小标题</h3><p>一句半到两句，不超过 30 字。</p></div></div>
      <div class="item"><span class="ordinal">03</span>
        <div><h3>小标题</h3><p>一句半到两句，不超过 30 字。</p></div></div>
    </div>
  </div>

  <p class="bottom-note" data-anim="rise" data-at="1500" data-dur="650" data-dy="7">脚注：限定条件或免责说明。</p>
  <span class="page-number">02 / 13</span>
  <div class="tmpl-brand">单位 · 项目名</div>
</section>
```

---

## 3. 价值行（四类对象各一行）

```html
<section class="slide paper" id="slide-3" aria-label="3 标题">
  <h2 data-anim="rise" data-at="0" data-dur="600" data-dx="-18" data-dy="0">标题</h2>

  <div class="value-rows" data-stagger="550" data-gap="170">
    <article data-emph="2200" data-emph-dur="1200">
      <span>对象一</span>
      <div><h3>这一行要能独立成句</h3><p>补充说明，一句话。</p></div>
    </article>
    <article data-emph="3050" data-emph-dur="1200">
      <span>对象二</span>
      <div><h3>这一行要能独立成句</h3><p>补充说明，一句话。</p></div>
    </article>
    <article data-emph="3900" data-emph-dur="1200">
      <span>对象三</span>
      <div><h3>这一行要能独立成句</h3><p>补充说明，一句话。</p></div>
    </article>
    <article data-emph="4750" data-emph-dur="1200">
      <span>对象四</span>
      <div><h3>这一行要能独立成句</h3><p>补充说明，一句话。</p></div>
    </article>
  </div>

  <p class="bottom-note" data-anim="rise" data-at="1500" data-dur="650" data-dy="7">脚注。</p>
  <span class="page-number">03 / 13</span>
  <div class="tmpl-brand">单位 · 项目名</div>
</section>
```

> 5 行时把 `data-gap` 调到 150，并删掉 `data-emph` 的逐行强调（改成只强调最后一行）。

---

## 4. 依据行（数据来源）

```html
<section class="slide paper" id="slide-4" aria-label="4 标题">
  <h2 data-anim="rise" data-at="0" data-dur="600" data-dx="-18" data-dy="0">数据依据：三个来源共同支撑</h2>

  <div class="source-rows" data-stagger="600" data-gap="220">
    <article data-emph="2200" data-emph-dur="1400"><b>来源一</b>
      <div><h3>材料名称与版本</h3><p>用来说明这份材料提供了什么字段。</p></div></article>
    <article data-emph="3350" data-emph-dur="1400"><b>来源二</b>
      <div><h3>材料名称与版本</h3><p>用来说明这份材料提供了什么字段。</p></div></article>
    <article data-emph="4500" data-emph-dur="1400"><b>来源三</b>
      <div><h3>材料名称与版本</h3><p>用来说明这份材料提供了什么字段。</p></div></article>
  </div>

  <p class="bottom-note" data-anim="rise" data-at="1600" data-dur="650" data-dy="7">哪些是参考值、哪些是实测值，必须在这里讲清楚。</p>
  <span class="page-number">04 / 13</span>
  <div class="tmpl-brand">单位 · 项目名</div>
</section>
```

---

## 5. 四宫格（原则 / 两层对照）

```html
<section class="slide paper" id="slide-5" aria-label="5 标题">
  <h2 data-anim="rise" data-at="0" data-dur="600" data-dx="-18" data-dy="0">标题</h2>

  <div class="rigor-grid" data-stagger="600" data-gap="200">
    <div>
      <span class="rule-index" data-emph="2300" data-emph-dur="1200">第一层</span>
      <h3>原则一</h3><p>两行以内，<br>必要时手动断行。</p>
      <span class="rule-index" data-emph="3250" data-emph-dur="1200">第二层</span>
      <h3>原则二</h3><p>两行以内，<br>必要时手动断行。</p>
    </div>
    <div>
      <span class="rule-index" data-emph="4200" data-emph-dur="1200">第三层</span>
      <h3>原则三</h3><p>两行以内，<br>必要时手动断行。</p>
      <span class="rule-index" data-emph="5150" data-emph-dur="1200">第四层</span>
      <h3>原则四</h3><p>两行以内，<br>必要时手动断行。</p>
    </div>
  </div>

  <p class="bottom-note" data-anim="rise" data-at="1600" data-dur="650" data-dy="7">脚注。</p>
  <span class="page-number">05 / 13</span>
  <div class="tmpl-brand">单位 · 项目名</div>
</section>
```

> 深色页把 `class="slide paper"` 换成 `class="slide dark"`，文字色自动跟随。

---

## 6. 表格（参数 / 设备 / 对照）

```html
<section class="slide paper" id="slide-6" data-hold="8600" aria-label="6 标题">
  <h2 data-anim="rise" data-at="0" data-dur="600" data-dx="-18" data-dy="0">标题</h2>

  <p class="future-caption" data-anim="rise" data-at="230" data-dur="550" data-dy="9">小标签：说明这是哪一阶段 / 哪一类</p>

  <table class="hardware">
    <thead data-anim="rise" data-at="430" data-dur="550">
      <tr><th>需要知道什么</th><th>可采用的设备或接口</th><th>用于什么决策</th></tr>
    </thead>
    <tbody data-stagger="700" data-gap="180">
      <tr data-emph="2100" data-emph-dur="1300"><td>短词条</td><td>一行半以内<br>可手动断行</td><td>一句结论</td></tr>
      <tr data-emph="2900" data-emph-dur="1300"><td>短词条</td><td>一行半以内</td><td>一句结论</td></tr>
      <tr data-emph="3700" data-emph-dur="1300"><td>短词条</td><td>一行半以内</td><td>一句结论</td></tr>
      <tr data-emph="4500" data-emph-dur="1300"><td>短词条</td><td>一行半以内</td><td>一句结论</td></tr>
    </tbody>
  </table>

  <p class="hardware-base" data-anim="rise" data-at="1400" data-dur="650">表下结论一句，用主色。</p>
  <p class="bottom-note" data-anim="rise" data-at="1700" data-dur="650" data-dy="7">脚注：口径与边界。</p>
  <span class="page-number">06 / 13</span>
  <div class="tmpl-brand">单位 · 项目名</div>
</section>
```

**6 行时**必须加 `data-hold="8600"`，否则强调还没走完就换页。

---

## 7. 四步流程

```html
<section class="slide paper" id="slide-7" aria-label="7 标题">
  <h2 data-anim="rise" data-at="0" data-dur="600" data-dx="-18" data-dy="0">标题</h2>

  <div class="flow-line" data-stagger="600" data-gap="180">
    <div data-emph="1900" data-emph-dur="1500"><b>01</b><h3>动词短语</h3><p>两行说明，<br>手动断行。</p></div>
    <div data-emph="3150" data-emph-dur="1500"><b>02</b><h3>动词短语</h3><p>两行说明，<br>手动断行。</p></div>
    <div data-emph="4400" data-emph-dur="1500"><b>03</b><h3>动词短语</h3><p>两行说明，<br>手动断行。</p></div>
    <div data-emph="5650" data-emph-dur="1500"><b>04</b><h3>动词短语</h3><p>两行说明，<br>手动断行。</p></div>
  </div>

  <div class="lower-statement" data-anim="rise" data-at="1250" data-dur="650">
    <strong>一句结论</strong>
    <p>补充说明，一句话。</p>
  </div>

  <p class="bottom-note" data-anim="rise" data-at="1600" data-dur="650" data-dy="7">脚注。</p>
  <span class="page-number">07 / 13</span>
  <div class="tmpl-brand">单位 · 项目名</div>
</section>
```

---

## 8. 三栏阶段（建议用深色页）

```html
<section class="slide dark" id="slide-8" aria-label="8 标题">
  <h2 data-anim="rise" data-at="0" data-dur="600" data-dx="-18" data-dy="0">三阶段路线：甲、乙、丙</h2>

  <div class="vision-line" data-stagger="600" data-gap="250">
    <article data-emph="2100" data-emph-dur="1500"><span>当前原型</span><h3>阶段一</h3><p>两行说明<br>手动断行</p></article>
    <article data-emph="3550" data-emph-dur="1500"><span>下一阶段</span><h3>阶段二</h3><p>两行说明<br>手动断行</p></article>
    <article data-emph="5000" data-emph-dur="1500"><span>进一步拓展</span><h3>阶段三</h3><p>两行说明<br>手动断行</p></article>
  </div>

  <div class="vision-result" data-anim="rise" data-at="1600" data-dur="850">
    <h2>一句收束，<br>可两行。</h2>
  </div>

  <p class="bottom-note" data-anim="rise" data-at="1900" data-dur="650" data-dy="7">脚注：哪些已实现、哪些是设想。</p>
  <span class="page-number">08 / 13</span>
  <div class="tmpl-brand">单位 · 项目名</div>
</section>
```

---

## 9. 左标题 + 右三条

```html
<section class="slide paper" id="slide-9" aria-label="9 标题">
  <h2 data-anim="rise" data-at="0" data-dur="600" data-dx="-18" data-dy="0">标题</h2>

  <div class="wearable-layout">
    <div class="wearable-goal" data-anim="rise" data-at="500" data-dur="850">
      <h2>左侧主张，<br>三行以内，<br>每行不超过八字。</h2>
      <p>补一句解释，<br>两行内。</p>
    </div>
    <div class="wearable-steps" data-stagger="700" data-gap="200">
      <article data-emph="2100" data-emph-dur="1450"><b>场景一</b><p>一句半说明。</p></article>
      <article data-emph="3350" data-emph-dur="1450"><b>场景二</b><p>一句半说明。</p></article>
      <article data-emph="4600" data-emph-dur="1450"><b>场景三</b><p>一句半说明。</p></article>
    </div>
  </div>

  <p class="bottom-note" data-anim="rise" data-at="1600" data-dur="650" data-dy="7">脚注。</p>
  <span class="page-number">09 / 13</span>
  <div class="tmpl-brand">单位 · 项目名</div>
</section>
```

---

## 10. 左标题 + 右三块

```html
<section class="slide paper" id="slide-10" aria-label="10 标题">
  <h2 data-anim="rise" data-at="0" data-dur="600" data-dx="-18" data-dy="0">标题</h2>

  <div class="vr-layout">
    <div class="vr-purpose" data-anim="rise" data-at="500" data-dur="850">
      <h2>左侧主张，<br>两到三行。</h2>
      <p>补一句解释，<br>两行内。</p>
    </div>
    <div class="vr-details" data-stagger="700" data-gap="200">
      <div data-emph="2100" data-emph-dur="1450"><h3>问什么</h3><p>两行说明，<br>手动断行。</p></div>
      <div data-emph="3350" data-emph-dur="1450"><h3>怎么做</h3><p>两行说明，<br>手动断行。</p></div>
      <div data-emph="4600" data-emph-dur="1450"><h3>留什么</h3><p>两行说明，<br>手动断行。</p></div>
    </div>
  </div>

  <p class="bottom-note" data-anim="rise" data-at="1600" data-dur="650" data-dy="7">脚注。</p>
  <span class="page-number">10 / 13</span>
  <div class="tmpl-brand">单位 · 项目名</div>
</section>
```

---

## 11. 图 + 文

图片建议先压到宽 1000 px 以内再 base64 内嵌，否则单文件会迅速超过 5 MB。

```html
<section class="slide paper" id="slide-11" aria-label="11 标题">
  <h2 data-anim="rise" data-at="0" data-dur="600" data-dx="-18" data-dy="0">标题</h2>

  <div class="space-layout">
    <div class="photo-frame" data-anim="rise" data-at="450" data-dur="1200" data-dy="20">
      <img src="data:image/png;base64,..." alt="图注：这张图是什么">
    </div>
    <div class="scenario-copy" data-anim="rise" data-at="800" data-dur="850" data-dx="20" data-dy="0">
      <h3>例如：一个具体场景</h3>
      <p>三个问句，<br>每句一行。</p>
      <div class="scenario-result" data-emph="2700" data-emph-dur="1800">先提出，<br>再验证。</div>
      <small>补一句适用范围。</small>
    </div>
  </div>

  <p class="bottom-note" data-anim="rise" data-at="1500" data-dur="650" data-dy="7">脚注。</p>
  <span class="page-number">11 / 13</span>
  <div class="tmpl-brand">单位 · 项目名</div>
</section>
```

---

## 12. 两栏备查

```html
<section class="slide paper" id="slide-12" aria-label="12 备查">
  <h2 data-anim="rise" data-at="0" data-dur="600" data-dx="-18" data-dy="0">备查：资料与参考</h2>

  <div class="reference-layout" data-stagger="550" data-gap="220">
    <section>
      <h3>本项目已有资料</h3>
      <p>材料一<br>材料二<br>材料三</p>
      <h3>方法与标准</h3>
      <p>标准一<br>标准二</p>
    </section>
    <section>
      <h3>后续技术参考</h3>
      <p>参考一<br>参考二<br>参考三<br>参考四</p>
    </section>
  </div>

  <p class="bottom-note" data-anim="rise" data-at="1500" data-dur="650" data-dy="7">哪些用于说明现状、哪些只是可选路径。</p>
  <span class="page-number">12 / 13</span>
  <div class="tmpl-brand">单位 · 项目名</div>
</section>
```

---

## 13. 收尾（深色）

```html
<section class="slide dark" id="slide-13" aria-label="13 收尾">
  <h2 data-anim="rise" data-at="0" data-dur="600" data-dx="-18" data-dy="0">一句总结标题</h2>

  <div class="value-close">
    <h2 data-anim="rise" data-at="500" data-dur="1100" data-dy="26">三行结论，<br>每行一句，<br>不超过十字。</h2>
    <p class="closing-main" data-anim="rise" data-at="1200" data-dur="850">一句收束，<br>说明边界。</p>
    <p class="closing-thanks" data-anim="rise" data-at="1900" data-dur="800">感谢各位评委</p>
  </div>

  <span class="page-number">13 / 13</span>
  <div class="tmpl-brand">单位 · 项目名</div>
</section>
```

---

## data-* 属性速查

| 属性 | 挂在哪 | 取值 | 含义 |
|---|---|---|---|
| `data-anim` | 单个元素 | `rise` / `drift` / `zoom` / `fade` | 入场方式 |
| `data-at` | 单元素 | 毫秒 | 延迟起点 |
| `data-dur` | 单元素 | 毫秒，默认 650 | 时长 |
| `data-dx` / `data-dy` | 单元素 | px，默认 0 / 22 | 位移量（`drift` 用 `dx="-26" data-dy="0"`） |
| `data-scale` | `zoom` | 默认 1.035 | 终态缩放 |
| `data-stagger` | 父容器 | 毫秒，默认 600 | 组内第一条的起点 |
| `data-gap` | 父容器 | 毫秒，默认 180 | 组内间隔 |
| `data-emph` | 组内元素或单元素 | 毫秒 | 强调起点 |
| `data-emph-dur` | 同上 | 毫秒，默认 1200 | 强调时长 |
| `data-hold` | `<section>` | 毫秒，默认 8000 | 本页总时长 |

时间预算公式：`末条强调起点 + data-emph-dur + 400ms` 应当 ≤ `data-hold`，否则会被下一页打断。
