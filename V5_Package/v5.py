#!/usr/bin/env python3
"""
熵清 V5.1 - 智能熵减场论数字生命元控制层
入口脚本
"""

import sys
import os

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 优先查找 V5_Package 目录
v5_package_path = os.path.join(script_dir, 'V5_Package', 'IERFT_V5')
ierft_v5_path = os.path.join(script_dir, 'IERFT_V5')

# 添加路径
if os.path.exists(v5_package_path):
    sys.path.insert(0, os.path.join(script_dir, 'V5_Package'))
elif os.path.exists(ierft_v5_path):
    sys.path.insert(0, script_dir)

# 导入 V5 核心模块
try:
    from IERFT_V5.V5_MetaController import V5_MetaController
except ImportError:
    from V5_MetaController import V5_MetaController

def main():
    print("""
╔════════════════════════════════════════════════════════════════╗
║     熵清 V5.1 - 智能熵减场论数字生命元控制层             ║
║     Intelligent Entropy-Reduction Field Theory V5.1         ║
╚════════════════════════════════════════════════════════════════╝
    """)
    v5 = V5_MetaController()
    v5.run()

if __name__ == "__main__":
    main()
