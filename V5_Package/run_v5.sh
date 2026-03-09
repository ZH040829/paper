#!/bin/bash
# IERFT V5 一键启动脚本 (Linux/macOS)
# 使用方法: ./run_v5.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
V5_DIR="$SCRIPT_DIR/V5_Package"

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║     熵清 V5.1 - 智能熵减场论数字生命                   ║"
echo "║     正在启动...                                        ║"
echo "╚════════════════════════════════════════════════════════════════╝"

# 检查 Python
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ 错误: 未找到 Python 解释器"
    echo ""
    echo "请安装 Python 3.7+ :"
    echo "  Ubuntu/Debian: sudo apt install python3"
    echo "  macOS: brew install python3"
    echo "  Windows: https://www.python.org/downloads/"
    read -p "按回车键退出..."
    exit 1
fi

# 检查版本
PY_VERSION=$($PYTHON_CMD -c 'import sys; print(sys.version_info.major)' 2>/dev/null)
if [ "$PY_VERSION" -lt 3 ]; then
    echo "❌ 错误: Python 版本过低 (需要 3.7+)"
    read -p "按回车键退出..."
    exit 1
fi

echo "✓ Python 解释器已就绪: $($PYTHON_CMD --version)"
echo ""

# 运行 V5
cd "$V5_DIR"
$PYTHON_CMD v5.py
EXIT_CODE=$?

echo ""
echo "════════════════════════════════════════════════════════════════"
echo "V5 已退出 (代码: $EXIT_CODE)"
echo "════════════════════════════════════════════════════════════════"
read -p "按回车键退出..."
