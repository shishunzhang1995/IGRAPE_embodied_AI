# M1–M2：Linux、Python、开发环境

[首页](README.md) · [日程](01-schedule.md) · [资料导航](05-resources.md) · [验收](06-assessment.md)

## M1：4 天学会科研开发必需的 Linux

目标是能够在终端完成工作，不要求 4 天学完 Linux。主线读 R02《鸟哥的 Linux 私房菜》的文件权限、目录、文件内容、Bash、数据流重定向与进程相关小节；用 R03 Missing Semester 的 Shell 练习补动手。跳过磁盘分区、内核编译、服务器搭建、SELinux 深入配置。鸟哥旧版的 CentOS／yum 指令不能原样当作 Ubuntu 安装教程。

### D1：装好可持续使用的系统

先记录 Windows 版本、CPU 架构、内存、可用磁盘、显卡。普通 CPU、8 GB 内存也可走精简路线；16 GB 内存更宽裕。建议为课程和 WSL 预留约 40 GB 可用空间，这是教学预算，不是官方系统最低要求。硬盘紧张时不下载大数据集或 Isaac Sim。

Windows 用户按 [Microsoft WSL 安装文档](https://learn.microsoft.com/en-us/windows/wsl/install)操作，在管理员 PowerShell 中执行：

```powershell
wsl --list --online
wsl --install -d Ubuntu-24.04
```

如提示重启，先重启，再打开 Ubuntu 创建普通用户名和密码。随后在 PowerShell 检查：

```powershell
wsl -l -v
```

版本列应为 2。若已有同名发行版，不要再次安装；先确认数据与版本。WSL 不可用时，先检查虚拟化、Windows 功能、网络与管理员权限；45 分钟仍无进展就提交错误给导师，转实验室 Ubuntu 账号继续学习。已有原生 Ubuntu、虚拟机或 Mac 的同学以能进入课程 Ubuntu 环境为准；不在第一天强制折腾双系统。

下列命令在 **Ubuntu 终端**运行，不是在 PowerShell：

```bash
cat /etc/os-release
uname -a
whoami
pwd
df -h
free -h
sudo apt update
sudo apt install -y git curl wget unzip build-essential python3 python3-venv
mkdir -p ~/embodied-foundations/{data,scripts,logs,results,reports}
```

项目放在 `~/embodied-foundations` 这类 Linux 主目录；初学阶段避免把大量训练小文件放在 `/mnt/c/` 下。先用 nano 或现有编辑器完成修改，不要求背 Vim 快捷键。

**微验收**：解释 PowerShell 与 Bash 的区别；指出主目录与 Windows 磁盘挂载目录；创建一个文件、退出 Ubuntu 后重新找到它。提交终端文本记录即可，不以大量截图代替证据。

### D2：文件、权限与查找

必须会用 `pwd`、`ls -lah`、`cd`、`mkdir -p`、`cp`、`mv`、`cat`、`less`、`head`、`tail`、`find`、`grep`、`wc`、`chmod`、`tar`、`man` 和 `--help`。每条命令都在课程测试目录内练习，尤其是删除与覆盖。

任务：建立 `raw/processed/scripts/logs`；准备 3 个文本文件；找到全部 `.txt`；筛选包含 `ERROR` 的行；统计行数；给脚本增加执行权限。解释相对路径、绝对路径、`rwx`、普通用户与 `sudo`。不要求记住所有参数，允许现场查帮助。

### D3：管道、日志、进程与环境变量

理解 `>` 覆盖、`>>` 追加、`2>&1` 合并错误输出、`|` 管道、`tee` 保留输出。会看 `ps`、`top`，用 Ctrl+C 停止前台程序；仅对本人测试进程练习 `kill`。了解 `PATH`、`which`、`export`，知道“命令不存在”与“文件不存在”不是同一个问题。

微任务：写一个循环打印 20 行状态的 Shell 脚本，每第 5 行打印 `ERROR`；记录日志并统计 4 行错误；换工作目录运行同一脚本；定位一个没有执行权限的报错。SSH／tmux 为选做，不要求学生自行配置公网服务器。

### D4：A1 综合交付

写 `env_report.sh` 输出时间、OS、用户、当前目录、Python 路径、磁盘和内存概况；写 `run_demo.sh` 生成上述 20 行日志、提取错误、汇总并打包结果。要求重复运行不混入上一次结果，输出路径清楚，不操作测试目录之外的文件。

交 `linux/` 目录与一页 README。导师现场换目录、撤销执行权限或改输入路径，让学生排错。详细合格线见 A1。

## M2：Python、Git 和环境管理

### 学习范围

R04 Python：基本类型、列表、字典、控制流、函数、模块、文件读写、异常；仅初步理解类与对象。R05 NumPy：shape、dtype、索引、切片、广播、矩阵乘法、按轴聚合。R03 Git：`init/status/add/commit/log/diff/branch/switch/merge`。不在本周学装饰器、元类或复杂软件工程。

每天的 Python 练习都写成 `.py` 文件，至少支持一次命令行运行；Notebook 可以帮助探索，但最终交付不能依赖“先手动执行某些单元格”的隐藏状态。

### D5–D6 小任务

编写 `summarize.py --input data.csv --output summary.json`：读取含 `sample_id,value,label` 的 CSV，计算有效数值的数量、均值和标准差，报告空值／坏值数量。测试正常文件、空文件、含坏值文件各一次。扩展为 NumPy 实现并解释输出 shape。画简单折线图、保存 PNG，不只弹出窗口。

在 Git 分支上增加一个命令行参数，合并回主分支；故意修改一行再用 diff 找到变化。 `.gitignore` 至少覆盖 `__pycache__/`、`.venv/`、`data/cache/`、`outputs/`、`ros_ws/build/`、`ros_ws/install/`、`ros_ws/log/`。需要提交的少量结果图放 `reports/`，不要整目录忽略。

### D8 环境配方

使用 R06 的 Linux 安装说明在 **WSL 的 Ubuntu 内**安装 Miniconda。Miniconda 是较小的 Conda 发行版；不需要同时安装完整 Anaconda。安装器架构与机器一致，按官方指引检查下载来源与校验值。初始化 Bash 后重新打开 Ubuntu 终端。

```bash
conda create -n embodied-basics python=3.11 pip -y
conda activate embodied-basics
python -m pip install numpy matplotlib scikit-learn opencv-python-headless
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
python -c "import sys, torch; print(sys.executable); print(torch.__version__); print(torch.rand(2,3)); print(torch.cuda.is_available())"
python -m pip check
```

本月先走 CPU；CPU 环境中 `torch.cuda.is_available()` 为 `False` 是正常现象。`opencv-python-headless` 用于读写图像文件，不提供 `imshow`；用保存的图片或 matplotlib 查看结果。需要摄像头窗口是选做，避免同时安装多个 OpenCV wheel 变体。

上述是基础配方，依赖版本会变化；**导师预演成功后冻结本届实际版本**，再发给全体学生。GPU 同学也先通过 CPU 自检，再依据 R07 安装选择器和 Windows／Linux 的驱动条件建立独立 GPU 环境，不把 CUDA 安装当成本月核心作业。

保存环境证据：

```bash
mkdir -p reports/environment
python --version > reports/environment/python.txt
python -m pip freeze > reports/environment/requirements-lock.txt
conda env export --no-builds > reports/environment/environment-full.yml
conda env export --from-history > reports/environment/environment-history.yml
```

说明：history 文件主要保存手动要求的 Conda 包，**不会替你完整记录 pip 安装内容**；完整导出、pip lock、安装命令和 PyTorch 索引地址要一起保存。导出文件中的机器绝对 `prefix` 不作为别人的路径要求。版本文件也不是跨所有 OS／CPU 架构的通用锁。

A2 复现时在同类系统新建 `embodied-replay`（Python 3.11），按原安装来源和锁定版本重新安装，运行同一自检和 CSV 脚本。下载耗时超过预算时先由导师提供预装环境继续任务，另约环境复验；不能把旧环境“还能跑”作为已经成功重建的证据。

### 两种终端，避免 Conda 与 ROS 混用

ML 终端：激活 `embodied-basics`。ROS 终端：退出 Conda，确认 `which python3` 是系统解释器，再 `source /opt/ros/jazzy/setup.bash`。Conda 的 Python 与 apt 安装的 ROS Python 绑定可能不兼容，参考 [ROS Python 包说明](https://docs.ros.org/en/jazzy/How-To-Guides/Using-Python-Packages.html)。

两个模块未来要联动时，初学阶段可用独立进程＋JSON／CSV／socket 边界；不要为了让两个环境互相 import 而随意改系统 Python。后续毕设再统一部署架构。

## 常见问题的最短排查顺序

| 现象 | 先检查 | 仍失败时 |
|---|---|---|
| WSL 装不上 | Windows 版本、虚拟化、重启、网络 | 交完整错误，转实验室 Ubuntu，保留安装复验 |
| `ModuleNotFoundError` | `which python`、`python -m pip --version`、当前环境 | 在正确环境装包，别反复对全局 pip 安装 |
| 下载慢或失败 | URL、网络、可用空间；记录来源 | 用导师统一缓存或文档认可的源，不拼凑未知脚本 |
| 权限错误 | 路径、文件属主、执行位 | 解释原因再修，避免给所有文件 `777` |
| ROS 找不到包 | Ubuntu／ROS 版本、source、build 是否成功 | 关闭 Conda 终端，在干净 ROS 终端复现 |
| 图形窗口打不开 | WSL 图形支持、DISPLAY、启动方式 | 切无图形节点；不让 GUI 阻断 ROS 主线 |

卡住 30 分钟应记录“目标、命令、完整错误、已尝试步骤”；45 分钟向导师或同伴求助。定位和解释错误本身也是学习成果。
