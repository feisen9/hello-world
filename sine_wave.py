#!/usr/bin/env python3
"""
生成正弦波图像的 Python 脚本
使用 matplotlib 绘制正弦波并保存为 SVG 格式
"""

import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体（可选，如果没有中文字体可注释掉相关行）
# plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 生成数据
x = np.linspace(0, 4 * np.pi, 1000)  # 0 到 4π，1000 个点
y = np.sin(x)  # 正弦波

# 创建图形
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制正弦波
ax.plot(x, y, 'b-', linewidth=2, label='sin(x)')

# 添加标题和标签
ax.set_title('Sine Wave (正弦波)', fontsize=16, fontweight='bold')
ax.set_xlabel('x (弧度)', fontsize=12)
ax.set_ylabel('sin(x)', fontsize=12)

# 添加网格
ax.grid(True, linestyle='--', alpha=0.7)

# 添加图例
ax.legend(loc='upper right')

# 设置 x 轴刻度为 π 的倍数
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 5*np.pi/2, 3*np.pi, 7*np.pi/2, 4*np.pi])
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π', '5π/2', '3π', '7π/2', '4π'])

# 设置 y 轴范围
ax.set_ylim(-1.5, 1.5)

# 添加水平参考线 y=0
ax.axhline(y=0, color='k', linewidth=0.5)

# 自动调整布局
plt.tight_layout()

# 保存为 SVG 格式
plt.savefig('sine_wave.svg', format='svg', bbox_inches='tight')
print("正弦波图像已保存为 sine_wave.svg")

# 也可以保存为 PNG 格式（可选）
# plt.savefig('sine_wave.png', dpi=300, bbox_inches='tight')
# print("正弦波图像已保存为 sine_wave.png")

plt.show()
