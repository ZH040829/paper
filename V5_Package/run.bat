@echo off
chcp 65001 >nul
title IERFT V5 - 智能熵减场论数字生命

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║     IERFT V5 - 智能熵减场论数字生命元控制层                ║
echo ║     Intelligent Entropy-Reduction Field Theory V5           ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo 启动 V5 元控制器...
echo.

python v5.py

if errorlevel 1 (
    echo.
    echo 错误：Python 未安装或未添加到 PATH
    echo 请安装 Python 3.7+ 并重试
    pause
)
