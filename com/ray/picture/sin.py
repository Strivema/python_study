
# -*- coding:utf-8 -*-
# @Author: Marie
# @Time:  2019/7/16 12:15 AM
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np
def main():
    # 指定采样的范围以及样本的数量
    x_values = np.linspace(0, 2 * np.pi, 1000)
    # 计算每个样本对应的正弦值
    y_values = np.sin(x_values)
    plt.plot(x_values, np.sin(2 * x_values), '--b')
    # 绘制折线图(线条形状为--, 颜色为蓝色)
    plt.plot(x_values, y_values, '--r')
    plt.show()


if __name__ == '__main__':
    main()