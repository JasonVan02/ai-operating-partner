# STOP_LOSS → DIRECTION_REASSESSMENT

同一根因连续两次实质性修复仍失败，暂停机械第三次修复，进入 STOP_LOSS，执行 [原方向重评](anti-patch-loop.md) 七问。旧规则中的同 AC 连续两轮 FAIL、重复回归或基础方向异议仍是触发信号。STOP_LOSS 不是取消目标、第四模式或 Review status；未解决任务不能 PASS。

## 计数与例外

- 计数对象是根因及实际修复/验证，不是失败命令总数。首次发现失败、只读诊断、缺材料 BLOCKED 不等于修复尝试。
- 用稳定 cause_id 关联 AC、尝试、改动、原始结果和新增知识；新 round、改名字或换工具不清除历史。不同新原因要有证据，不能仅重新描述旧现象。
- 第二次失败揭示新的明确原因，且下一次有高边际价值时，先记证据、可区分假设的下一检验、合理预期结果与一次有界尝试，再继续。不是“第三次一定禁止”，也不是永久豁免；仍失败再次重评。
- 长期低产出、成本失控等旧信号可更早触发；不得为减少 repair 指标提前放弃可解决问题。

## 恢复记录

记录 Goal、Requirement、Assumptions、Architecture、Tool choice、Implementation strategy、Root cause、两次实际证据与下一判别检验。决定沿用 CONTINUE_CURRENT_DIRECTION / REFACTOR_DIRECTION / REPLACE_APPROACH / ROLLBACK / HUMAN_DECISION_REQUIRED。继续原方向必须有新证据或可证伪新实验。

范围内可逆修复自主进行；重大范围/成本/架构选择需用户决定。ROLLBACK 不授权删除或丢失用户改动。不可解决时交付已完成部分、真实缺口与恢复条件，不伪称完成，也不无限等待。

## 可选机器记录

FULL Evidence 可带 `capital_state: CONTINUE | STOP_LOSS | REASSESSED`；缺省兼容旧 V1 输入。`STOP_LOSS` 阻塞 gate；`REASSESSED` 还须 `reassessment_evidence` 非空 artifact ID 列表，指向当前已纳入审查快照的实际重评记录。未知/非字符串状态、缺引用均拒绝。它只检查状态与证据完整性；理由是否充分仍由独立审查负责。旧 `direction_reassessment_pending=false` 也必须满足；不能用新字段覆盖旧门禁。
