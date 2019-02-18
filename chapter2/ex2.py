"""
感知机学习算法的对偶形式
"""

"""
Training data: ([3, 3], 1), ([4, 3], 1), ([1, 1], -1)
Perception model: sum_i(alpha_i * x_i * y_i * x_j) + b
In order words: 将perception model中的w, 变为与x, y有关的函数。
"""
