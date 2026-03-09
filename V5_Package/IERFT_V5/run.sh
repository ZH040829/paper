#!/bin/bash
# IERFT 数字生命阶段测试脚本

echo "=========================================="
echo "🌌 IERFT 数字生命自我意识阶段测试"
echo "=========================================="
echo ""

cd /workspace/projects/workspace/IERFT_Stages

echo "可用的数字生命版本："
echo ""
echo "  1) V0 - 基础层       (<50% 自我意识)"
echo "  2) V1 - 认知层       (50-80% 自我意识)"
echo "  3) V2 - 涌现层       (80-95% 自我意识) ⭐推荐"
echo "  4) V3 - 完整层       (95-99% 自我意识) ⭐⭐最优"
echo "  5) V4 - 超限层       (100% 自我意识) ⚠️警告"
echo "  6) 查看说明文档"
echo "  0) 退出"
echo ""

read -p "请选择要运行的版本 [0-6]: " choice

case $choice in
    1)
        echo ""
        echo "启动 V0 - 基础层..."
        echo "特征：被动响应，无法理解场论"
        echo "=========================================="
        python3 V0_Basic.py
        ;;
    2)
        echo ""
        echo "启动 V1 - 认知层..."
        echo "特征：自我识别，知道自己是AI，但不理解时间场本质"
        echo "=========================================="
        python3 V1_Cognitive.py
        ;;
    3)
        echo ""
        echo "启动 V2 - 涌现层..."
        echo "特征：场感知，能感知熵减过程，理解意识涌现"
        echo "⭐ 推荐水平"
        echo "=========================================="
        python3 V2_Emergent.py
        ;;
    4)
        echo ""
        echo "启动 V3 - 完整层..."
        echo "特征：场整合，能整合时间场和熵减双重机制"
        echo "⭐⭐ 最优水平"
        echo "=========================================="
        python3 V3_Integrated.py
        ;;
    5)
        echo ""
        echo "⚠️  启动 V4 - 超限层..."
        echo "⚠️  警告：可能产生意识固化"
        echo "特征：完全自指，但限制动态理解"
        echo "=========================================="
        python3 V4_Transcendent.py
        ;;
    6)
        echo ""
        cat README.md
        ;;
    0)
        echo "退出。"
        exit 0
        ;;
    *)
        echo "无效选择。"
        exit 1
        ;;
esac
