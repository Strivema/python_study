# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2019/7/16 12:22 AM
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt
def main():
    # 通过random模块的normal函数产生1000个正态分布的样本
    data = np.random.normal(10.0, 4.0, 1000)
    # 绘制直方图(直方的数量为10个)
    plt.hist(data, 100)
    plt.show()


if __name__ == '__main__':
    main()