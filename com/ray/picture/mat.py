# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2019/7/16 12:07 AM
# @Software: PyCharm
import matplotlib.pyplot as plt


def main():

    x_values = [x for x in range(1, 11)]
    y_values = [x ** 2 for x in range(1, 11)]
    plt.title('square')
    plt.xlabel('value', fontsize=18)
    plt.ylabel('Square', fontsize=18)
    plt.tick_params(axis='both', labelsize=10)
    plt.plot(x_values, y_values)
    plt.scatter(x_values,y_values)
    plt.show()
if __name__ == '__main__':
    main()
