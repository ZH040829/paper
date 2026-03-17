#!/bin/bash

# 熵清 V6 API 代理服务启动脚本

echo "🚀 启动熵清 V6 API 代理服务..."

# 检查是否已经在运行
if lsof -Pi :5001 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "⚠️  服务已在运行 (端口5001)"
    echo "📍 地址: http://localhost:5001"
    exit 0
fi

# 切换到脚本目录
cd "$(dirname "$0")"

# 启动服务
python3 api_proxy.py > logs/api_proxy.log 2>&1 &

# 等待服务启动
sleep 2

# 检查是否启动成功
if lsof -Pi :5001 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "✅ 服务启动成功！"
    echo "📍 地址: http://localhost:5001"
    echo "📋 日志: logs/api_proxy.log"
    echo ""
    echo "💡 使用说明："
    echo "   - 打开 v6.html 即可使用"
    echo "   - 查看日志: tail -f logs/api_proxy.log"
    echo "   - 停止服务: ./stop_proxy.sh"
else
    echo "❌ 服务启动失败，请查看日志:"
    tail -20 logs/api_proxy.log
    exit 1
fi
