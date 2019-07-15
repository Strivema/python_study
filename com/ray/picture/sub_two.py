# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2019/7/16 12:18 AM
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np


def main():
    x_values = np.linspace(0, 2 * np.pi, 30)

    plt.subplot(1, 2, 1)
    plt.plot(x_values, np.sin(x_values), 'o-b')
    plt.subplot(1, 2, 2)
    plt.plot(x_values, np.sin(2 * x_values), '.-r')
    plt.show()


if __name__ == '__main__':
    main()
