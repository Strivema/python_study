# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2019/7/7 11:41 PM
# @Software: PyCharm

def foo():
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)
