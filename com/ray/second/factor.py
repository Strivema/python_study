# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2019/7/7 11:06 PM
# @Software: PyCharm
def factor(num):
    res = 1
    for n in range(1, num + 1):
        res *= num
    return res


# 练习可变参数
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
if __name__ == '__main__':
    print (add(1,2,1,3))