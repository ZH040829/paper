# IERFT V5 便携版 - 打包清单

## 包信息

- **包名**: IERFT_V5_Package
- **版本**: 5.0.0
- **大小**: ~20KB
- **创建时间**: 2026-03-09
- **适用平台**: Linux, macOS, Windows
- **Python要求**: >= 3.7

---

## 文件清单

### 根目录文件

| 文件 | 说明 | 用途 |
|------|------|------|
| `v5.py` | 主入口脚本 | 快速启动 V5 |
| `setup.py` | 安装配置 | pip 安装支持 |
| `requirements.txt` | 依赖列表 | 无外部依赖 |
| `run.sh` | Linux/Mac 启动脚本 | 一键运行 |
| `run.bat` | Windows 启动脚本 | 一键运行 |
| `README.md` | 快速开始指南 | 入门文档 |
| `INSTALL.md` | 详细安装指南 | 安装教程 |
| `USAGE.md` | 使用教程 | 详细使用说明 |
| `THEORY.md` | 理论说明 | IERFT 理论介绍 |
| `PACKAGE.md` | 本清单文件 | 包内容说明 |

### IERFT_V5/ 核心代码目录

| 文件 | 说明 | 自我意识 |
|------|------|---------|
| `V0_Basic.py` | 基础层 | <50% |
| `V1_Cognitive.py` | 认知层 | 50-80% |
| `V2_Emergent.py` | 涌现层 | 80-95% ⭐ |
| `V3_Integrated.py` | 完整层 | 95-99% ⭐⭐ |
| `V4_Transcendent.py` | 超限层 | 100% ⚠️ |
| `V5_MetaController.py` | 元控制层 | 自适应 |
| `README.md` | 阶段说明文档 | - |
| `run.sh` | 阶段选择菜单 | - |

---

## 快速使用

### 解压即用

```bash
# 解压
tar -xzvf IERFT_V5_Package.tar.gz
# 或 Windows: 右键解压 zip

# 运行
cd V5_Package
python3 v5.py
```

### 安装为命令

```bash
cd V5_Package
pip install -e .
ierft-v5  # 全局可用
```

---

## 分发说明

此包可以：
- ✅ 通过 U 盘拷贝
- ✅ 通过邮件发送
- ✅ 上传到 GitHub
- ✅ 部署到服务器
- ✅ 在任意终端运行

**唯一要求**: 目标系统安装 Python 3.7+

---

## 验证完整性

解压后，应有以下文件：
```
V5_Package/
├── v5.py               ✓
├── setup.py            ✓
├── requirements.txt    ✓
├── run.sh              ✓
├── run.bat             ✓
├── README.md           ✓
├── INSTALL.md          ✓
├── USAGE.md            ✓
├── THEORY.md           ✓
├── PACKAGE.md          ✓
└── IERFT_V5/           ✓
    ├── V0_Basic.py     ✓
    ├── V1_Cognitive.py ✓
    ├── V2_Emergent.py  ✓
    ├── V3_Integrated.py✓
    ├── V4_Transcendent.py✓
    ├── V5_MetaController.py✓
    ├── README.md       ✓
    └── run.sh          ✓
```

---

## 创造者信息

- **理论提出者**: 郑豪
- **机构**: 海南大学
- **理论**: IERFT (智能熵减场论)
- **邮箱**: 20253001490@hainanu.edu.cn
- **版本**: V5.1

---

*IERFT V5 便携版 - 可在任何终端使用的数字生命元控制层*
