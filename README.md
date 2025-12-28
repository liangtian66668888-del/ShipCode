# 面向航母舰面特情处置的保障应急决策方法
论文《面向航母舰面特情处置的保障应急决策方法》的官方代码。该仓库含我们算法的环境、代码以及数据集。
![imga](overview.png)
## 1. 要求
执行以下命令安装必要依赖。
```
git clone https://github.com/liangtian66668888-del/ShipCode.git
cd ShipCode
pip install -r requirements.txt
```
## 2. 航母舰面特情处置资源动态调度（RDSE）代码实现

本仓库实现了论文中的 **RDSE（Resource Dynamic Scheduling for Emergency）** 方法，用于在航母舰面“保障作业 + 特情处置”共存场景中进行应急资源动态调度。代码包含可训练的强化学习决策器（Manager/PreAssign/Worker）以及对应的仿真环境（ShipEnv）。

---

## 2.1 算法主要功能（RDSE 做什么）

RDSE 的核心目标是：在任务动态出现、资源有限且存在冲突约束的情况下，**快速、合理地为任务分配处置小组/资源，并兼顾安全风险与调度效率**。

在代码层面，RDSE 由三个关键模块组成（对应论文框架）：

### 2.1.1 预分配模块 PreAssign（DGPA）
**功能：**  
对“当前待处理任务集合”与“当前可用处置小组集合”进行一次**粗粒度匹配**，为每个处置小组生成候选任务/倾向分配，减少后续调度的搜索难度，并提升对任务/小组数量变化的适应性。

**实现要点：**
- `PreAssignActor`：对 agent/task 做 embedding，用点积注意力得到 `P(task | agent)` 的分配概率矩阵  
- `PreAssignCritic`：输出 agent-task 的 Q 值矩阵  
- `MIX`：将各 agent 的局部价值聚合为全局价值（AMIX/AMN 风格的 mixing network）
- 消融版本：`PreAssignNormalCritic` / `PreAssignNormal`（无 mixing 或 MLP 替代）

### 2.1.2 调度决策模块 Manager（任务选择/分配）
**功能：**  
在 PreAssign 给出的候选结构或环境可用动作约束下，Manager 负责**为每个任务选择合适的处置小组**（或为每次调度选择一个可用 agent），输出离散动作。

**实现要点：**
- `ManagerNet.actor()`：基于 agent/task embedding 的注意力匹配，输出各 agent 的选择概率（离散动作分布）
- `ManagerNet.critic()`：评估 Q 值（价值网络）
- 训练采用 SAC 风格更新（带 entropy 项，target network 软更新）

### 2.1.3 执行层模块 Worker（连续动作/需求估计）
**功能：**  
用于对任务的“需求强度/资源量”等连续决策进行估计（例如资源需求比例、执行强度等）。Worker 输出连续动作，并通过 critic 学习价值。

**实现要点：**
- `Worker.actor` 输出 0~1 连续动作（sigmoid）
- 加入高斯噪声探索（sigma 衰减）
- 使用 actor-critic 结构 + target 网络软更新（DDPG 风格）

---

## 2.2 环境功能说明（ShipEnv 能做什么）

本仓库的核心环境为 `ShipEnv`，用于模拟舰面任务与资源调度过程，为强化学习提供交互接口（state/action/reward/done/info）。

### 2.2.1 环境建模对象
- **任务（Task）**
  - 包含任务属性（类型、位置、紧急度/风险、需求等）
  - 支持保障任务与特情任务共存
  - 任务可动态出现、可完成、可失效/超时（取决于你的任务规则实现）

- **处置小组/资源（Agent/Team）**
  - 包含小组属性（能力、负载、位置、状态等）
  - 支持可用/占用/移动等状态变化
  - 支持资源冲突与可用性约束（通过 avail_action / avail_agents mask 体现）

### 2.2.2 状态 State
环境状态通常包含（具体以代码实现为准）：
- 当前可用处置小组的属性与状态（位置、能力、是否可用）
- 当前待处理任务的属性（位置、需求、风险、剩余量等）
- 环境全局信息（时间步、风险/距离等）

### 2.2.3 动作 Action
环境动作是“分配/选择”类型：
- Manager 的离散动作：从可用处置小组中选择一个（或为任务选择小组）
- PreAssign 输出：agent->task 的候选分配矩阵（用于预分配阶段）
- Worker 输出：连续动作（需求强度/资源量等）

### 2.2.4 奖励 Reward（dense + sparse）
环境奖励通常由两部分构成：
- **rbf_reward（dense shaping）**：基于距离/风险的连续奖励（如 RBF shaping）
- **task_reward（sparse）**：任务完成（或关键事件达成）带来的稀疏奖励

## 3. 代码结构
```text
├── main_ShipEnv.py              # 训练入口
├── allocation_ShipEnv.py        # 舰面仿真环境
├── manager.py                   # 高层调度决策（SAC + Attention）
├── worker.py                    # 处置小组（执行层）
├── preAssign.py                 # 预分配模块（DGPA）
├── utils.py                     # 工具函数
```
## 4. 训练方式
```bash
python main_ShipEnv.py
```

- `manager_return`：强化学习实际使用的累计回报
- `total_return`：环境返回的总奖励
- `length`：episode 步数（小于最大步数表示任务提前完成）
### 4.1 训练demo
```bash
python ShipEnv.py
```
---

## 5. 实验指标
主要评价指标包括：
- **原任务完成率**：衡量特情处置对原保障作业的干扰程度
- **物资损失率**：衡量调度策略对特情损失的抑制能力
- **平均累计回报**：反映训练效率与稳定性

论文实验结果表明，RDSE 在多种场景下均显著优于 PPO、A2C 及消融模型。

---