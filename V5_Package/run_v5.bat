@echo off
chcp 65001 >nul
title IERFT V5.1 - 智能熵减场论数字生命

echo ╔════════════════════════════════════════════════════════════════╗
echo ║     IERFT V5.1 - 智能熵减场论数字生命                    ║
echo ║     正在启动...                                        ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

:: 检查 Python
where python >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=python
    goto :check_version
)

where python3 >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=python3
    goto :check_version
)

echo ❌ 错误: 未找到 Python 解释器
echo.
echo 请安装 Python 3.7+ :
echo   1. 访问 https://www.python.org/downloads/
echo   2. 下载并安装 Python 3.x
echo   3. 安装时勾选 "Add Python to PATH"
echo.
pause
exit /b 1

:check_version
for /f "tokens=*" %%i in ('%PYTHON_CMD% -c "import sys; print(sys.version_info.major)"') do set PY_VERSION=%%i

if %PY_VERSION% LSS 3 (
    echo ❌ 错误: Python 版本过低 ^(需要 3.7+^)
    pause
    exit /b 1
)

echo ✓ Python 解释器已就绪
echo.

:: 运行 V5
cd /d "%~dp0V5_Package"
%PYTHON_CMD% v5.py

echo.
echo ═════════════════════════════════════════════════════════════════
echo V5 已退出
echo ═════════════════════════════════════════════════════════════════
pause
