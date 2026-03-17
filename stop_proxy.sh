#!/bin/bash

# 熵清 V6 API 代理服务停止脚本

echo "🛑 停止熵清 V6 API 代理服务..."

# 查找并杀死进程
PID=$(lsof -ti :5001 2>/dev/null)

if [ -n "$PID" ]; then
    kill $PID
    sleep 1

    # 检查是否停止成功
    if lsof -Pi :5001 -sTCP:LISTEN -t >/dev/null 2>&1; then
        echo "⚠️  正常停止失败，强制停止..."
        kill -9 $PID
    fi

    echo "✅ 服务已停止"
else
    echo "ℹ️  服务未运行"
fi
