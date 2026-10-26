# 资料导航：只学本阶段指定的部分

[首页](README.md) · [每日安排](01-schedule.md)

核对日期：2026-10-26。优先使用作者教材、课程主页与官方文档。下面的“预算”是本课程建议投入的阅读／观看时间，**不是原视频总时长**，已包含在 95 小时之内；学生按不懂的概念查阅，不需要逐项刷完。中文为主、英文官方文档用于核对 API 与版本。

## 必修资料与限定范围

| 编号 | 入口／语言／形式 | 本月只学什么 | 使用日／建议资料预算 |
|---|---|---|---|
| R01 | [Microsoft WSL 安装](https://learn.microsoft.com/zh-cn/windows/wsl/install)、[开发环境](https://learn.microsoft.com/en-us/windows/wsl/setup/environment)，中／英，官方文档 | 安装指定发行版、检查 WSL2、Linux 用户、文件位置 | D1，约 30 分钟，安装另计动手时间 |
| R02 | [鸟哥的 Linux 私房菜](https://www.vbird.org/)，繁中，免费在线教材 | 基础学习篇中的文件权限／目录、文件内容、Bash、重定向、进程；按标题找，不强依赖不同版本章号 | D2–D4，共约 90 分钟查阅 |
| R03 | [Missing Semester 中文](https://missing-semester-cn.github.io/)、[MIT 原课程](https://missing.csail.mit.edu/)，中／英，讲义与视频 | 选 2020 版“课程概览与 Shell”“Shell 工具和脚本”“版本控制 Git”；日志处理按需查 | D2–D3、D6，共约 90 分钟 |
| R04 | [Python 官方中文教程](https://docs.python.org/zh-cn/3/tutorial/)，中文，文档 | 3–5 章选读；模块、输入输出、错误异常相关小节 | D5，约 45 分钟；不熟 Python 者用选做时间补 |
| R05 | [NumPy 初学者指南](https://numpy.org/doc/stable/user/absolute_beginners.html)，英文，示例 | array、shape、dtype、indexing、broadcasting、axis | D6，约 30 分钟 |
| R06 | [Miniconda／Anaconda 官方安装入口](https://www.anaconda.com/docs/getting-started/installation)、[Conda 环境管理](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html)，英文，文档 | 选 Miniconda Linux 安装；create/activate/export、conda 与 pip | D8，约 30 分钟 |
| R07 | [PyTorch 安装选择器](https://pytorch.org/get-started/locally/)、[Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html)，英文，官方教程 | tensor、autograd、数据加载、模型、优化、保存加载；优先 CPU | D8、D12–D13，约 100 分钟，代码练习另计 |
| R08 | [动手学深度学习中文版](https://zh.d2l.ai/)、[李沐配套课程与 B 站视频入口](https://courses.d2l.ai/zh-v2/)，中文，教材＋视频 | 2.3–2.6 按需复习；3.1、4.1、4.4、4.5；6.2–6.6 | D9、D11–D12、D15、D17，共约 150 分钟选段 |
| R09 | [scikit-learn 入门](https://scikit-learn.org/stable/getting_started.html)，英文，官方示例 | fit/predict、transform、Pipeline、划分与交叉验证概念；从该页进入指标文档 | D9–D11，共约 60 分钟 |
| R10 | [OpenCV Python 教程](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)，英文，官方示例 | 图像读写、颜色转换、阈值、轮廓；几何变换选读 | D16、D18，共约 60 分钟 |
| R11 | [ROS 2 Jazzy Ubuntu 安装](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)，英文，官方 | Ubuntu 24.04、软件源、desktop、开发工具、环境与 talker/listener | D19，约 30 分钟 |
| R12 | [ROS 2 Jazzy Tutorials](https://docs.ros.org/en/jazzy/Tutorials.html)，英文，官方；[鱼香 ROS](https://fishros.com/)，中文，配套课程 | Beginner CLI：node/topic/service/parameter；Client libraries：workspace/package、Python pub/sub；launch、rosbag 入门 | D19–D24，共约 150 分钟选段 |
| R13 | [Modern Robotics 作者视频配套页](https://modernrobotics.northwestern.edu/nu-gm-book-resource/)，英文，教材配套视频 | 刚体运动部分的坐标系、旋转、变换概念；本月计算限制在二维 | D23，约 25 分钟 |
| R14 | [PyTorch Geometric Introduction by Example](https://pytorch-geometric.readthedocs.io/en/latest/get_started/introduction.html)，英文，官方 | 节点特征、edge_index、消息传递概念；本月核心自己写 4 节点聚合 | D25，约 35 分钟 |
| R15 | [LeRobot 文档](https://huggingface.co/docs/lerobot/index)，英文，官方 | 从 Tutorials 进入 Imitation Learning for Robots；识别观测、动作、数据与策略接口 | D26，约 20 分钟 |
| R16 | [LeRobot 项目文档入口](https://huggingface.co/docs/lerobot/index)，英文，官方 | 安装和硬件页仅作架构与依赖阅读；本月不要求安装整个生态 | D26，约 10 分钟，与 R15 合并 |
| R17 | [Physical Intelligence openpi](https://github.com/Physical-Intelligence/openpi)，英文，作者仓库 | README 中模型、配置、推理／训练、数据格式；只做方向地图，不下载权重 | D26 选读 10 分钟，替换 R16 阅读 |
| R18 | [Isaac Sim 5.1.0 硬件要求](https://docs.isaacsim.omniverse.nvidia.com/5.1.0/installation/requirements.html)，英文，官方版本文档 | 硬件、驱动、Compatibility Checker；从同版本导航进入入门教程 | D26，约 15 分钟；实际演示为选做 |

## B 站观看入口

- **李沐《动手学深度学习》**：从[作者课程表](https://courses.d2l.ai/zh-v2/)进入每个主题的 B 站链接，优先使用该页关联的 PyTorch 版本；只看线性回归、MLP、过拟合、卷积与池化相关部分。此入口已打开核对，课程表有 B 站视频指向。
- **鱼香 ROS《动手学 ROS 2》**：[B 站课程](https://www.bilibili.com/video/BV1gr4y1Q7j5/)。检索已确认课程存在；选节点通信、CLI、Python 发布订阅。早期版本课程只作概念辅助。
- **鱼香 ROS《ROS 2 机器人开发从入门到实践》**：[B 站课程入口](https://www.bilibili.com/video/BV1GW42197Ck/)，可同时从[作者主页](https://fishros.com/)寻找配套内容。网页播放器可能有访问限制；具体分 P 名称和可播放状态由开课前普通浏览器确认。

不要求学生两套 ROS 课程同时看。若视频和 Jazzy 官方文档不一致，按课程统一环境和官方 API 修订。每个标准学习日观看／阅读默认不超过 45 分钟，超过部分放选做或只查关键片段。

## 资料阅读方法

先看当天提交物，再带着问题读资料；读一个概念就运行一个最小例子。记录“输入是什么、输出是什么、为什么这样写、改一个条件会怎样”。不要把抄讲义、截图或看完多少 P 当作掌握证据。

数学查漏只补当前任务用得上的内容。传统机器学习和深度学习是主线；遗传算法、模糊系统、群智能等传统“计算智能”方向本月不展开，除非毕设明确需要。强化学习本月只建立概念，不加完整算法训练任务。

## 核验与版本说明

已打开核对：鸟哥首页、Missing Semester 中文、D2L 教材与课程表、PyTorch 安装、Conda 管理、Python、NumPy、scikit-learn、OpenCV、Modern Robotics、PyG、LeRobot、openpi、Isaac Sim 要求页。网页可访问不代表学生网络或视频播放必然可用。

ROS 文档网页触发自动访问防护，因此改用[官方 Jazzy 文档源码：安装页](https://raw.githubusercontent.com/ros2/ros2_documentation/jazzy/source/Installation/Ubuntu-Install-Debs.rst)和[Python 包说明](https://raw.githubusercontent.com/ros2/ros2_documentation/jazzy/source/How-To-Guides/Using-Python-Packages.rst)核对了 Ubuntu 24.04 配对、talker/listener 和 Python 解释器兼容问题。源码中的 `{DISTRO}` 为文档模板变量，不是要粘贴到终端的字面命令。

本计划固定 Ubuntu／ROS 路线，但不伪造一套“已在学生硬件全面验证”的依赖锁。导师预演后把实际 Python、torch、torchvision、numpy、sklearn 与 ROS 包版本归档；下届开课重新核对。Isaac Sim 5.1.0 是用于说明硬件核对方法的固定参考版本，实验室如果选择其他版本，须整套使用对应版本文档。

失效链接处理：查作者主页同名章节 → 查官方仓库 → 由导师替换资源表并记日期。不寻找来历不明的盗版整书 PDF，不因单个视频失效停掉当日动手任务。
