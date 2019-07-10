# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2019/7/9 11:59 PM
# @Software: PyCharm
# 跑马灯
import os
import time
import random


def main_right():
    content = 'hello world'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.3)
        content = content[1:] + content[0]


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


#   查找第一大和第二大的数
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


def main_tri():
    num = int(input('num:'))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col])
        print()


# 约瑟夫环
def ring():
    persons = [True] * 30
    count, index, num = 0, 0, 0
    while count < 15:
        if persons[index]:
            num += 1
        if num == 9:
            persons[index] = False
            count += 1
            num = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非')


if __name__ == '__main__':
    # main_right()
    # print (generate_code(5))
    # print (get_suffix('lll.xxx', True))
    # print (max2([11,22,33,44]))
    # print (main_tri())
    print(ring())
