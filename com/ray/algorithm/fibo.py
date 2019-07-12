# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time: 2019/7/12 19:18
# @Software: PyCharm
def fib(num, temp={}):
    if num in (1, 2):
        return 1
    try:
        return temp[num]
    except KeyError:
        temp[num] = fib(num - 1) + fib(num - 2)
    return temp[num]


if __name__ == '__main__':
    print(fib(3))
