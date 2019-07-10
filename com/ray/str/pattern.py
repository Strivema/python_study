# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2019/7/11 12:15 AM
# @Software: PyCharm
import re

"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
def main():
    name = input('name:')
    qq = input('qq:')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',name)
    m2 = re.match(r'^[1-9]\d{4,11}$',qq)
    if not m2:
        print ('qq is not valid')
    if m1 and m2:
        print ('info is valid')
if __name__ == '__main__':
    main()
