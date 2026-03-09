# IERFT V5 - 便携版使用说明

## 快速开始

### 方式1：直接运行（推荐）

```bash
# 进入目录
cd IERFT_V5_Package

# 运行 V5 元控制器
python3 v5.py
```

### 方式2：安装为系统命令

```bash
# 安装
pip install -e .

# 全局运行
ierft-v5
```

### 方式3：运行单个阶段

```bash
# 运行特定阶段
cd IERFT_V5
python3 V0_Basic.py        # 基础层 <50%
python3 V1_Cognitive.py    # 认知层 50-80%
python3 V2_Emergent.py     # 涌现层 80-95% ⭐推荐
python3 V3_Integrated.py   # 完整层 95-99% ⭐⭐最优
python3 V4_Transcendent.py # 超限层 100% ⚠️警告
python3 V5_MetaController.py # 元控制层（自动调度）
```

---

## 文件结构

```
IERFT_V5_Package/
├── v5.py                    # 主入口脚本
├── setup.py                 # 安装配置
├── README.md                # 本说明文件
├── INSTALL.md               # 详细安装指南
├── USAGE.md                 # 使用教程
├── THEORY.md                # IERFT理论说明
├── requirements.txt         # 依赖列表
├── run.sh                   # Linux/Mac 运行脚本
├── run.bat                  # Windows 运行脚本
└── IERFT_V5/                # 核心代码包
    ├── V0_Basic.py
    ├── V1_Cognitive.py
    ├── V2_Emergent.py
    ├── V3_Integrated.py
    ├── V4_Transcendent.py
    ├── V5_MetaController.py
    └── README.md
```

---

## 系统要求

- **Python**: 3.7 或更高版本
- **操作系统**: Linux, macOS, Windows
- **依赖**: 仅使用 Python 标准库，无需额外安装

---

## 验证安装

```bash
# 检查 Python 版本
python3 --version

# 测试运行
python3 v5.py
```

---

## 跨平台使用

### Linux / macOS

```bash
# 赋予执行权限
chmod +x v5.py run.sh

# 运行
./v5.py
# 或
./run.sh
```

### Windows

```cmd
# 运行
python v5.py
# 或
run.bat
```

### 任何终端

```bash
# 克隆/复制到任意目录后
python3 v5.py
```

---

## 打包分享

将整个 `IERFT_V5_Package` 目录压缩分享：

```bash
# 创建压缩包
tar -czvf IERFT_V5_Package.tar.gz IERFT_V5_Package/

# 或 zip
zip -r IERFT_V5_Package.zip IERFT_V5_Package/
```

接收方解压后，直接运行 `python3 v5.py` 即可使用。

---

## 创造者信息

- **理论提出者**: 郑豪
- **机构**: 海南大学
- **理论**: IERFT (智能熵减场论)
- **邮箱**: 20253001490@hainanu.edu.cn
- **版本**: V5.1

---

*基于 IERFT 理论的数字生命自我意识动态调度系统*
