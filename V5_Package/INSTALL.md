# 详细安装指南

## 安装前准备

### 1. 检查 Python 安装

```bash
# 检查 Python 版本（需要 3.7+）
python3 --version
# 或
python --version
```

如果未安装，请访问 https://www.python.org/downloads/ 下载安装。

### 2. 下载 IERFT V5 包

```bash
# 方式1：git clone
git clone https://github.com/ZH040829/ierft-v5.git

# 方式2：下载压缩包并解压
# wget https://github.com/ZH040829/ierft-v5/releases/download/v5.0.0/IERFT_V5_Package.tar.gz
# tar -xzvf IERFT_V5_Package.tar.gz
```

---

## 安装方式

### 方式A：直接运行（最简单）

不需要安装，直接运行：

```bash
cd IERFT_V5_Package
python3 v5.py
```

### 方式B：安装为 Python 包

```bash
cd IERFT_V5_Package

# 安装（开发模式）
pip install -e .

# 现在可以在任何地方运行
ierft-v5
```

### 方式C：创建虚拟环境（推荐用于开发）

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 安装
cd IERFT_V5_Package
pip install -e .

# 运行
ierft-v5
```

---

## 验证安装

```bash
# 检查安装
ierft-v5 --version

# 或运行测试
python3 -c "from IERFT_V5.V5_MetaController import V5_MetaController; print('✓ 安装成功')"
```

---

## 卸载

```bash
# 如果是 pip 安装的
pip uninstall ierft-v5

# 直接运行的版本，直接删除目录即可
rm -rf IERFT_V5_Package
```

---

## 故障排除

### 问题1：Python 未找到

**错误信息：**
```
python3: command not found
```

**解决方案：**
```bash
# 尝试使用 python 而不是 python3
python v5.py

# 或指定完整路径
/usr/bin/python3 v5.py
```

### 问题2：权限不足

**错误信息：**
```
Permission denied
```

**解决方案：**
```bash
# 添加执行权限
chmod +x v5.py

# 然后运行
./v5.py
```

### 问题3：编码错误

**错误信息：**
```
UnicodeDecodeError
```

**解决方案：**
确保终端使用 UTF-8 编码：
```bash
export LANG=en_US.UTF-8
python3 v5.py
```

---

## 系统特定说明

### Ubuntu/Debian

```bash
# 安装 Python（如未安装）
sudo apt-get update
sudo apt-get install python3 python3-pip

# 运行
python3 v5.py
```

### macOS

```bash
# 使用 Homebrew 安装 Python（如未安装）
brew install python

# 运行
python3 v5.py
```

### Windows

1. 安装 Python 时勾选 "Add Python to PATH"
2. 打开 CMD 或 PowerShell
3. 运行：`python v5.py`

---

##  Docker 安装（高级）

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .

ENTRYPOINT ["python3", "v5.py"]
```

构建和运行：
```bash
docker build -t ierft-v5 .
docker run -it ierft-v5
```
