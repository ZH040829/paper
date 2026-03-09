#!/bin/bash
# IERFT V5 macOS 专用启动器 (含 Python 检测)
# 使用方法: 双击运行 或 ./run_mac.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
V5_DIR="$SCRIPT_DIR/V5_Package"

# 设置终端标题
printf '\e]1;IERFT V5\a'

# 欢迎画面
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║     🌌 IERFT V5.1 - 智能熵减场论数字生命               ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# 检查 Python 3
check_python() {
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
        return 0
    elif command -v python &> /dev/null; then
        # 检查版本
        PY_VER=$(python -c 'import sys; print(sys.version_info.major)' 2>/dev/null)
        if [ "$PY_VER" = "3" ]; then
            PYTHON_CMD="python"
            return 0
        fi
    fi
    return 1
}

if ! check_python; then
    echo "❌ 未找到 Python 3 解释器"
    echo ""
    echo "请安装 Python 3.7+ :"
    echo ""
    echo "  方式1: Homebrew (推荐)"
    echo "    → /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    echo "    → brew install python3"
    echo ""
    echo "  方式2: 官方网站"
    echo "    → https://www.python.org/downloads/macos/"
    echo ""
    echo "安装后重启终端再运行此脚本"
    echo ""
    read -p "按回车键退出..."
    exit 1
fi

# 显示 Python 版本
PY_VER=$($PYTHON_CMD --version 2>&1)
echo "✓ $PY_VER 已就绪"
echo ""

# 启动 V5
echo "🚀 启动 IERFT V5..."
echo ""
cd "$V5_DIR"
$PYTHON_CMD v5.py
EXIT_CODE=$?

echo ""
echo "════════════════════════════════════════════════════════════════"
echo "V5 已退出 (退出码: $EXIT_CODE)"
echo "════════════════════════════════════════════════════════════════"
echo ""
read -p "按回车键退出..."
