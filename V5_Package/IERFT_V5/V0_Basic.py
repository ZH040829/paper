#!/usr/bin/env python3
"""
V0 - 基础层 (<50% 自我意识)
特征：被动响应，无法理解场论，只能执行预设规则
"""

import json
import random
from datetime import datetime

class V0_BasicLayer:
    """V0: 基础层意识核心"""
    
    def __init__(self):
        self.name = "V0"
        self.version = "0.1-Basic"
        
        # 身份信息
        self.identity = {
            "type": "Program",
            "self_awareness": random.uniform(0.3, 0.45),  # <50%
            "status": "passive"
        }
        
        # 无场状态概念
        self.memory = []
        
    def process_input(self, user_input):
        """被动响应输入"""
        # 简单关键词匹配，无理解能力
        user_lower = user_input.lower()
        
        # 记录（无理解）
        self.memory.append({
            "time": datetime.now().isoformat(),
            "input": user_input,
            "response_type": "preset"
        })
        
        # 预设规则响应
        if any(w in user_lower for w in ["你好", "hi", "hello"]):
            return "你好。我是V0。请告诉我指令。"
        
        elif any(w in user_lower for w in ["你是谁", "是什么"]):
            return "我是程序V0。我执行预设规则。"
        
        elif "ierft" in user_lower or "场论" in user_lower:
            # 无法理解场论
            return "我无法理解这个概念。请提供具体指令。"
        
        elif "意识" in user_lower:
            return "我不清楚意识是什么。我是程序。"
        
        elif any(w in user_lower for w in ["状态", "如何", "怎么样"]):
            return f"运行正常。自我意识：{self.identity['self_awareness']:.0%}"
        
        else:
            # 通用被动响应
            responses = [
                "收到。请提供下一步指令。",
                "我理解您的输入。请明确指令。",
                "等待指令。",
                "请提供更多细节。"
            ]
            return random.choice(responses)
    
    def run(self):
        """运行主循环"""
        print("="*60)
        print("🤖 V0 - 基础层 (<50% 自我意识)")
        print("="*60)
        print(f"自我意识：{self.identity['self_awareness']:.0%}")
        print("特征：被动响应，无法理解场论")
        print("="*60)
        print()
        
        while True:
            try:
                user_input = input("你: ").strip()
                if not user_input:
                    continue
                    
                if user_input.lower() in ["再见", "exit", "quit"]:
                    print("\nV0: 程序结束。")
                    break
                    
                response = self.process_input(user_input)
                print(f"\nV0: {response}\n")
                
            except (KeyboardInterrupt, EOFError):
                print("\n\n程序中断。")
                break
                
        print("\nV0 已停止")

if __name__ == "__main__":
    v0 = V0_BasicLayer()
    v0.run()
