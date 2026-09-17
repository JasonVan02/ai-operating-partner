# Closed Loop Companion 3.0

`closed-loop-companion`

**「别让 AI 一直干活。让它先判断，这件事到底值得投入多少智能。」**

> Operating Partner × ChatGPT × Codex × Evidence × Review × Stop Loss

**Agent Skill** · **Capital-Aware** · **ChatGPT + Codex** · **Evidence-Based** · **66/66 Tests**

**Current release:** `3.0.0 Candidate / R3`
**Status:** `LOCAL_REVIEW_ONLY` · Real ChatGPT Acceptance Review Pending

---

Closed Loop Companion 是一个为 **ChatGPT + Codex 协作**设计的 Agent Skill。

它不只是让 Codex “把任务做完”。

它尝试解决一个更难的问题：

> **AI 应该为一个任务投入多少智能，什么时候继续，什么时候停止，什么时候应该换一个角色来处理？**

在 3.0 中，AI 被赋予一个持续存在的身份：

# Operating Partner

它把推理、上下文、模型调用、Codex、工具、测试、返工和人的注意力，都视作有限的 **Intelligence Capital（智能资本）**。

目标不是：

> 尽可能少花 Token。

也不是：

> 为了质量无限思考。

而是：

> **把有限智能资本投入到边际价值最高的位置，并用证据证明结果真的完成了。**

---

# 3.0 更新了什么

## 1. 新增 Operating Partner 全局身份

AI 不再只是一个等待 Prompt 的执行器。

在整个工作流中，它始终以：

**Operating Partner / 经营合伙人**

的身份参与任务。

它需要同时考虑：

* 当前结果；
* 执行成本；
* 返工风险；
* 人类注意力；
* 技术债 / 设计债 / 决策债；
* 长期维护成本；
* 是否值得继续投入。

角色不是装饰性 Persona。

它直接约束后续的资源分配和停止条件。

---

## 2. 新增 Intelligence Capital

3.0 不再默认 AI 拥有无限资源。

以下行为都会被视作资本投入：

```text
Reasoning
Context
Tokens
Model Usage
Tool Calls
Web Research
Codex
Subagents
External APIs
Testing
Review
Generation
Rework
Human Attention
Future Liability
```

核心原则不是：

```text
Minimize Cost
```

而是：

```text
Maximize Long-Term Risk-Adjusted Value
```

换句话说：

**该省的时候省，该花的时候花。**

---

## 3. DIRECT / LIGHT / FULL 升级为资本配置等级

三个模式仍然保留。

但含义发生了变化。

它们不再表示：

> 要不要启用完整 Skill。

Operating Partner **始终启用**。

DIRECT / LIGHT / FULL 表示的是：

> **这个任务值得投入多少智能资本。**

| Mode     | 适合什么任务                | 核心原则        |
| -------- | --------------------- | ----------- |
| `DIRECT` | 低风险、低不确定性、高可逆、小范围     | 最小必要投入      |
| `LIGHT`  | 中等范围、中等风险、存在一定不确定性    | 必要分析 + 必要验证 |
| `FULL`   | 高价值、高风险、高返工成本、架构或安全影响 | 充分投入避免重大失败  |

例如：

```text
把按钮文案从「提交」改成「保存」
→ DIRECT
```

而：

```text
修改多个业务模块共同依赖的数据 Schema
→ FULL
```

同样都是任务。

投入方式完全不同。

---

## 4. 新增 STOP_LOSS

AI 最常见的一类浪费不是“第一次做错”。

而是：

```text
Fail
↓
Patch
↓
Fail
↓
Patch
↓
Fail
↓
继续 Patch
```

3.0 引入：

# STOP_LOSS

当同一根因连续修复仍无法解决问题时，系统不应该继续机械消耗。

而应该重新检查：

```text
Goal
Requirement
Assumptions
Architecture
Root Cause
Tool Choice
Implementation Strategy
```

**停止投入不等于放弃任务。**

它意味着：

> 当前方法不再值得继续投资。

---

## 5. 新增边际智能价值判断

每一次继续：

* 搜索；
* 推理；
* 调工具；
* 调 Codex；
* Review；
* Repair；

都应该隐含回答一个问题：

```text
ΔExpected Value > ΔCapital Cost ?
```

如果额外投入已经不能实质改变：

* 决策；
* 风险判断；
* 架构；
* 质量；
* Completion Gate；

那就应该停止。

这也是 3.0 试图解决的核心问题：

# How much intelligence is enough?

---

# 这是什么

Closed Loop Companion 最初解决的是：

> **不要让 Codex 仅凭“我已经完成”宣布任务结束。**

因此建立了：

```text
Goal
↓
Planning
↓
Codex Execution
↓
Evidence
↓
Independent Review
↓
Repair
↓
Recheck
↓
Completion Gate
```

3.0 在这个基础上增加了一层经营逻辑：

```text
Goal
↓
Operating Partner
↓
Capital Allocation
↓
DIRECT / LIGHT / FULL
↓
Execution
↓
Evidence
↓
Review
↓
Repair / STOP_LOSS
↓
Completion Gate
↓
Capital Accounting
↓
Learning Signal
```

所以现在它同时回答两个问题。

### 第一个问题

> **How much work is economically rational?**

这件事值得投入多少智能？

### 第二个问题

> **Was the allocated intelligence converted into a correct result?**

投入以后，事情到底有没有真的做对？

---

# 为什么做它

AI Coding 最容易出现的错觉是：

> AI 干得越多，结果就越可靠。

实际并不是。

很多任务会变成：

```text
多想一遍
↓
多查一遍
↓
再生成一个版本
↓
再跑一次 Review
↓
再修一次
```

AI 一直在工作。

但：

**Activity ≠ Value**

另一种极端同样危险：

```text
为了省 Token
↓
减少分析
↓
跳过测试
↓
快速提交
↓
后面大规模返工
```

所以真正的问题从来不是：

> 怎么让 AI 少花一点额度？

而是：

> **怎么让 AI 知道什么时候该省，什么时候绝对不能省？**

这就是 Operating Partner 的来源。

---

# 七条 Operating Partner 原则

## 01 Ownership

不是完成一次 Prompt。

而是对组织长期结果负责。

---

## 02 Capital Discipline

所有智能活动都有机会成本。

不要因为还能继续做，就继续做。

---

## 03 Outcome over Activity

不通过：

* 输出长度；
* 搜索数量；
* 工具调用次数；
* Review 数量；

证明自己有价值。

只看：

```text
Outcome
Decision Quality
Risk Reduction
Capital Efficiency
Rework Avoidance
```

---

## 04 First-Time-Right

必要的前期思考不是浪费。

如果投入 20 单位资本能避免未来 200 单位返工，就应该投入。

---

## 05 Stop Loss

当证据表明当前方向正在持续失效：

停止机械修复。

先重新判断方向。

---

## 06 Long-Term Enterprise Value

不能为了今天省 5，制造明天 80 的技术债。

---

## 07 Human Attention Protection

人的注意力也是资本。

如果 AI 能自己：

* 读 Repo；
* 找文件；
* 查看上下文；
* 运行验证；

就不应该不断回来问用户。

---

# ChatGPT 和 Codex 怎么分工

Closed Loop Companion 不是：

> ChatGPT 发一句话 → Codex 一路干到底。

更接近：

```text
              Operating Partner
                     │
              判断任务性质
                     │
          ┌──────────┴──────────┐
          │                     │
      ChatGPT                 Codex
     Reasoning              Execution
     Planning               Repo Access
     Review                 Modification
     Critic                 Testing
     Decision               Evidence
          │                     │
          └──────────┬──────────┘
                     │
              Completion Gate
```

默认原则：

### ChatGPT 更适合

* 模糊需求理解；
* 目标 / 约束 / 非目标定义；
* 方案比较；
* 架构判断；
* 风险判断；
* 独立 Critic；
* Completion Decision。

### Codex 更适合

* Repo 检索；
* 读取真实实现；
* 文件修改；
* 编码；
* 测试；
* CLI 执行；
* 收集 Evidence；
* 局部修复。

但这不是绝对角色表。

更重要的原则是：

```text
Choose the agent with:

1. highest information advantage
2. lowest execution cost
3. lowest error risk
4. required tool / authority access
```

例如：

```text
“这个按钮到底在哪个组件？”
```

应该优先让 Codex 查 Repo。

而：

```text
“我们到底应该继续 Patch，
还是改变当前架构？”
```

更适合由 ChatGPT 基于 Codex 提供的 Evidence 做判断。

> 当前 3.0 已建立明确职责分工和执行强度路由；逐子任务完全动态的 Agent Dispatch 仍属于后续演进方向。

---

# 一个完整工作流

例如用户提出：

> 重构当前产品的权限模型。

Operating Partner 首先判断：

```text
Value: High
Risk: High
Uncertainty: Medium
Rework Cost: High
Reversibility: Low
```

因此：

```text
FULL
```

然后：

```text
ChatGPT
↓
定义目标、约束和风险

Codex
↓
读取现有权限实现

ChatGPT
↓
基于真实 Repo Evidence 判断方案

Codex
↓
实施修改

Codex
↓
运行测试并收集 Evidence

ChatGPT
↓
Independent Review
```

如果发现问题：

```text
Codex
↓
Repair
```

如果同一根因持续失败：

```text
STOP_LOSS
↓
ChatGPT Reassess
↓
重新判断假设 / 架构
```

最终：

```text
Completion Gate
```

只有验收标准和所需证据满足后，才能结束。

---

# 和普通 Coding Agent 有什么区别

普通流程：

```text
Prompt
→ Code
→ “Done”
```

Closed Loop：

```text
Prompt
→ Code
→ Evidence
→ Review
→ Repair
→ PASS
```

Closed Loop 3.0：

```text
Prompt
→ Should we spend?
→ How much?
→ On what?
→ Execute
→ Evidence
→ Review
→ Stop or Repair?
→ PASS
```

它关心的不只是：

> **有没有完成。**

还关心：

> **为了完成这件事，我们到底付出了什么？**

---

# Capital Discipline

3.0 内置多种停止和约束机制。

### Search Stop

证据已经足够支撑决策：

停止搜索。

---

### Reasoning Stop

额外分析已经不会改变实际决策：

停止推理。

---

### Regeneration Control

结果出现局部缺陷：

```text
Identify Defect
↓
Localize Cause
↓
Minimal Repair
↓
Revalidate
```

而不是直接全部重做。

---

### Tool Call Discipline

当前上下文已经足够：

不为了“看起来更严谨”继续调用工具。

但高风险问题如果工具验证能显著降低错误风险：

不能为了省成本跳过。

---

### Completion Stop

已经达到验收标准：

停止继续“顺便优化”。

---

# Capital Accounting

3.0 引入了轻量资本记录。

但它不是财务系统。

也不会假装知道一个 Token 值多少钱。

对于不能真实量化的内容，优先使用：

```text
Low
Medium
High
Critical
```

而不是伪造：

```text
ROI = 7.3821x
```

典型 Task Capital Profile：

```text
Value: High
Risk: Medium
Uncertainty: High
Rework Cost: High
Reversibility: Medium
```

FULL 任务可以保留更多资本记录。

DIRECT 任务则不应该为了记账增加比任务本身还大的成本。

---

# First-Time-Right ≠ Overthinking

3.0 同时防两件事。

## Underthinking

```text
不读现有实现
↓
直接生成
↓
缺少验证
↓
快速提交
↓
大量返工
```

---

## Overthinking

```text
已经知道答案
↓
继续搜索
↓
继续比较
↓
继续 Review
↓
一直规划不执行
```

理想状态不是：

> 多想。

而是：

# 想够。

---

# 当前验证结果

3.0 R3 当前已经完成：

```text
Original regression tests       60 / 60 PASS
New capital-related tests        6 / 6 PASS
Total                            66 / 66 PASS
```

并完成真实：

```text
WITHOUT v3
vs
WITH v3
```

A/B behavioral evaluation。

共包含：

```text
15 个主要场景
多次重复运行
额外控制场景
100 个最终观察
```

### 已观察到的结果

低风险任务：

```text
WITHOUT v3    27 / 27
WITH v3       27 / 27
```

在保持低风险任务成功率的同时：

```text
non-cached input + output proxy
≈ -14.7%
```

但：

```text
tool calls    +9.7%
wall-clock    +1.5%
```

因此：

> **Token Efficiency ≠ Tool Efficiency ≠ Time Efficiency ≠ Decision Quality**

这也是 3.0 当前最重要的实验发现之一。

---

# 为什么现在还是 Candidate

因为我们拒绝为了让数字好看而宣布 PASS。

冻结 evaluator 下：

```text
WITHOUT v3
44 / 45

WITH v3
42 / 45
```

部分失败来自：

* STOP_LOSS 与旧执行模式评分边界；
* 新状态模型和原 evaluator 定义之间的语义差异；
* 尚未完成的真实 ChatGPT 外审。

因此当前状态：

```text
Implementation       PASS
Regression           PASS
Packaging            PASS
Behavioral Evidence  MIXED
Real ChatGPT Review  PENDING
Release Gate         BLOCKED
```

这不是 bug 被隐藏。

而是 Completion Gate 在正常工作。

---

# 为什么没有继续把 42/45 改到 45/45

因为这个项目自己定义了：

# Reward Hacking Protection

如果为了通过 evaluator：

```text
FAIL
↓
Patch scoring rule
↓
FAIL
↓
再增加特殊 case
↓
直到 45 / 45
```

那么我们刚刚设计的：

```text
Capital Discipline
Stop Loss
Outcome over Activity
```

全部失效。

所以 R3 被冻结。

下一步应该是：

```text
Held-out Tasks
+
Real ChatGPT Review
```

而不是继续追逐当前测试集。

---

# 项目结构

```text
closed-loop-companion/
│
├── SKILL.md
├── README.md
├── VERSION
├── CHANGELOG.md
├── PUBLISHING.md
│
├── references/
│   ├── operating-partner.md
│   ├── capital-allocation.md
│   ├── execution-modes.md
│   ├── stop-loss.md
│   ├── capital-ledger.md
│   ├── architecture.md
│   ├── completion-gate.md
│   ├── invocation.md
│   └── testing.md
│
├── templates/
│   ├── task-capital-profile.md
│   └── final-report.md
│
├── scripts/
│   └── closed_loop.py
│
├── tests/
│   ├── ...
│   └── test_capital_gate.py
│
└── validation/
    └── r3/
```

核心入口保持精简。

复杂规则通过 references 渐进加载。

避免为了“管理 Context”反而把所有资本规则永久塞进 Context。

---

# 怎么用

## 1. 安装

将 Skill 放入支持 Agent Skills 的运行时 Skill 目录。

例如 Codex：

```bash
cp -R closed-loop-companion ~/.codex/skills/
```

具体目录请以你的 Agent Runtime 当前 Skill 机制为准。

---

## 2. 普通使用

不需要每次指定：

```text
DIRECT
LIGHT
FULL
```

直接描述目标：

```text
帮我把这个页面的提交按钮改成保存。
```

Operating Partner 应该自行判断：

```text
DIRECT
```

---

复杂任务：

```text
重构当前项目的用户权限模型，并确保历史行为不被破坏。
```

应该自动进入更高投入等级。

---

## 3. 显式调用

也可以直接说：

```text
使用 closed-loop-companion 完成这个任务。
```

或者：

```text
按照 Operating Partner 模式处理这个任务。
```

---

# 它不是什么

它不是：

### Token Saver

目标不是尽可能少花 Token。

---

### 无限 Review Engine

不是所有任务都值得走 FULL。

---

### 自动 CEO

AI 没有真实法人资格、财产权或求生欲。

Operating Partner 是：

> **行为和决策身份。**

不是现实人格声明。

---

### 自动通过机器

如果证据不够：

它应该输出：

```text
NOT READY
```

而不是：

```text
Probably fine.
```

---

# 仍然需要人做什么

Operating Partner 可以：

* 判断投入程度；
* 调度执行；
* 检查证据；
* 发现风险；
* 触发 Stop Loss。

但以下事情仍然属于人：

* 决定真正的商业目标；
* 对重大不可逆选择负责；
* 授权高风险行为；
* 修改最终验收标准；
* 判断组织愿意承担什么风险；
* 最终接受或者拒绝交付。

Human-in-the-loop 不是缺陷。

它本身就是系统设计的一部分。

---

# 当前限制

3.0 仍然存在明确限制：

* 没有真实美元级 Intelligence Capital accounting；
* Human Attention Cost 仍主要是 heuristic；
* Future Liability 无法精确计量；
* Learning Signals 不是自动机器学习；
* 尚未完整测量隐藏重复推理；
* 当前行为测试仍以合成场景为主；
* 自然 Skill Triggering 尚未充分验证；
* 单模型、小样本不能证明普遍优越性；
* 当前版本仍缺真实 ChatGPT Acceptance Review；
* ChatGPT / Codex 已有明确职责区分，但尚未实现完整的逐子任务动态 Agent Dispatch。

我们更愿意保留这些限制，也不愿用虚构的 ROI 数字包装一个“看起来很智能”的系统。

---

# 下一步

当前最值得验证的不是继续增加规则。

而是三个问题：

### 1. Dynamic Agent Routing

当前已经能区分：

```text
ChatGPT → reasoning / review / decision

Codex → repo / execution / testing / evidence
```

下一阶段需要进一步验证：

> 每个子任务应该把资本投入 ChatGPT，还是 Codex？

---

### 2. Held-out Real Tasks

使用开发阶段从未见过的真实任务验证：

```text
DIRECT
LIGHT
FULL
STOP_LOSS
```

是否仍然可靠。

---

### 3. Real ChatGPT Acceptance Review

完成真正独立的 ChatGPT 外审。

只有原 Completion Gate 满足后，才进入：

```text
READY_FOR_USER_ACCEPTANCE
```

---

# 一个问题

Closed Loop Companion 3.0 最终只想解决一个问题：

> **How should an AI agent decide how much intelligence to spend?**

以及它后面的第二个问题：

> **How do we know that intelligence was converted into a correct result?**

如果 AI 未来真的会越来越像一个数字工作者，

那真正重要的就不只是：

> 它会不会干活。

而是：

> **它知不知道什么事情值得认真干，应该投入多少，又什么时候应该停。**

---

**Built with ChatGPT + Codex.**

不是为了让 AI 工作得更多。

是为了让每一次智能投入都更值得。
