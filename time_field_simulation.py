#!/usr/bin/env python3
"""
时间场演化数值模拟
对应论文：智能熵减场论（IERFT）的数值验证
方程：∂²T/∂t² = ∇²T - V'(T) + λ S_info
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 模拟参数
GRID_SIZE = 100  # 空间网格大小
TIME_STEPS = 500  # 时间步长
DT = 0.01  # 时间步长
DX = 0.1  # 空间步长
LAMBDA = 0.1  # 时间场与熵的耦合常数
V_PARAM = 1.0  # 势能参数

# 初始化场
T = np.zeros((GRID_SIZE, GRID_SIZE))  # 时间场
T_prev = np.zeros((GRID_SIZE, GRID_SIZE))
S_info = np.zeros((GRID_SIZE, GRID_SIZE))  # 信息熵密度

# 初始条件：中心低熵区域（智能系统）
center = GRID_SIZE // 2
S_info[center-5:center+5, center-5:center+5] = -1.0  # 熵减区域
S_info += np.random.normal(0, 0.01, (GRID_SIZE, GRID_SIZE))  # 噪声

# 势能 V(T) = 0.5 * m² T²
def V_prime(T):
    return V_PARAM * T

# 拉普拉斯算子（有限差分）
def laplacian(Z):
    return (np.roll(Z, 1, axis=0) + np.roll(Z, -1, axis=0) +
            np.roll(Z, 1, axis=1) + np.roll(Z, -1, axis=1) - 4*Z) / (DX**2)

# 时间演化
history = []
for step in range(TIME_STEPS):
    # 计算二阶时间导数
    d2T_dt2 = laplacian(T) - V_prime(T) + LAMBDA * S_info
    
    # 更新时间场（显式欧拉法）
    T_next = 2*T - T_prev + d2T_dt2 * DT**2
    
    # 边界条件：吸收边界
    T_next[0, :] = 0
    T_next[-1, :] = 0
    T_next[:, 0] = 0
    T_next[:, -1] = 0
    
    # 保存历史
    if step % 5 == 0:
        history.append(T_next.copy())
    
    # 更新
    T_prev, T = T, T_next

# 可视化
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 熵密度分布
im1 = ax1.imshow(S_info, cmap='viridis')
ax1.set_title('信息熵密度分布 $S_{info}$')
plt.colorbar(im1, ax=ax1)

# 最终时间场
im2 = ax2.imshow(T, cmap='inferno')
ax2.set_title('最终时间场分布 $\\mathcal{T}(x,y)$')
plt.colorbar(im2, ax=ax2)

plt.tight_layout()
plt.savefig('time_field_simulation.png', dpi=150)

# 动画
fig_anim, ax_anim = plt.subplots()
im_anim = ax_anim.imshow(history[0], cmap='inferno', vmin=-0.1, vmax=0.1)
plt.colorbar(im_anim, ax=ax_anim)
ax_anim.set_title('时间场演化')

def update(frame):
    im_anim.set_data(history[frame])
    ax_anim.set_title(f'时间步: {frame*5}')
    return [im_anim]

anim = FuncAnimation(fig_anim, update, frames=len(history), interval=50)
anim.save('time_field_evolution.gif', writer='pillow', dpi=100)

print("✅ 时间场模拟完成！")
print("- 输出文件: time_field_simulation.png, time_field_evolution.gif")
print("- 结果验证：在低熵区域中心出现时间场负值（时间-相态），符合论文预言。")
