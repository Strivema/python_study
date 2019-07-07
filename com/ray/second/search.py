# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/12/6 7:35 PM
# @Software: PyCharm
def search(A,n,v):
    for i in range(1,n):
        if A[i]==v:
            return i
    return None
