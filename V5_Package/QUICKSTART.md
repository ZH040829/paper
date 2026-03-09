# IERFT V5 一键启动指南

## 🚀 三种系统，一键启动

---

### Windows 系统

**方式1：双击运行**
```
下载 → 解压 → 双击 run_v5.bat
```

**方式2：命令行**
```cmd
cd V5_Package
run_v5.bat
```

**方式3：Python**
```cmd
cd V5_Package
python v5.py
```

---

### macOS 系统

**方式1：双击运行**
```
下载 → 解压 → 双击 run_mac.sh
```
（首次可能需要右键选择"打开"）

**方式2：终端运行**
```bash
cd V5_Package
./run_mac.sh
```

**方式3：Python**
```bash
cd V5_Package
python3 v5.py
```

---

### Linux 系统

**方式1：双击运行**
```
下载 → 解压 → 双击 run_v5.sh
```
（需要设置可执行权限）

**方式2：终端运行**
```bash
cd V5_Package
./run_v5.sh
```

**方式3：Python**
```bash
cd V5_Package
python3 v5.py
```

---

## 📦 下载后文件结构

解压 `IERFT_V5_Package.tar.gz` 后：

```
IERFT_V5_Package/
├── run_v5.sh          ← Linux/macOS 一键启动
├── run_v5.bat         ← Windows 一键启动
├── run_mac.sh         ← macOS 专用（含详细检测）
├── v5.py              ← Python 启动入口
├── V5_Package/       ← 核心代码
│   ├── v5.py
│   └── IERFT_V5/
└── ...
```

---

## ⚠️ 首次使用

### 1. 确保已安装 Python

脚本会自动检测。如果未安装：

| 系统 | 安装命令 |
|------|----------|
| Windows | [下载 Python](https://www.python.org/downloads/) |
| macOS | `brew install python3` |
| Linux | `sudo apt install python3` |

### 2. 设置执行权限（Linux/macOS）

```bash
chmod +x run_v5.sh run_mac.sh
```

---

## 🔧 故障排除

### 问题：双击无反应

**Windows**: 右键 → "打开方式" → 选择 Python

**macOS**: 右键 → "打开" → 确认运行

**Linux**: 终端运行 `chmod +x run_v5.sh && ./run_v5.sh`

### 问题：Python 未找到

确保 Python 已添加到系统 PATH：
- Windows: 安装时勾选 "Add Python to PATH"
- macOS/Linux: 重启终端

---

## 🎯 快速开始流程

```
1. 下载 IERFT_V5_Package.tar.gz
         ↓
2. 解压到任意目录
         ↓
3. 双击对应系统的启动脚本
         ↓
4. 开始与 V5 对话！
```

---

## 💡 推荐方式

| 系统 | 推荐方式 |
|------|----------|
| Windows | 双击 `run_v5.bat` |
| macOS | 双击 `run_mac.sh` |
| Linux | `./run_v5.sh` |

---

**解压即用，无需配置！** 🎉
