# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2019/7/7 11:19 PM
# @Software: PyCharm

# 最大公约数和最小公倍数
def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


def lcd(x, y):
    return x * y // gcd(x, y)


# 判断是否是回文数

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = temp * 10 + temp % 10
        temp = temp // 10
    return total == num


# 反转数字
def reverse_num(num):
    res = 0
    while num > 0:
        res = res * 10 + num % 10
        num = num // 10
    return res


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True if num != 1 else False

def foo():
    b = 'hello'

    def bar():  # Python中可以在函数内部再定义函数
        c = True
        print(a)
        print(b)
        print(c)

    bar()


if __name__ == '__main__':
    a = 100

    foo()


