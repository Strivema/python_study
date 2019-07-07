# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2019/7/7 8:25 PM
# @Software: PyCharm

# 将8个苹果分成四组每组至少一个苹果有多少种方案。

import factor as f
def combine():
    m = int(input('m='))
    n = int(input('n='))
    fm = 1
    fn = 1
    fmn = 1
    for num in range(1, m + 1):
        fm *= num
    for num in range(1, n + 1):
        fn *= num
    for num in range(1, m - n + 1):
        fmn *= num
    ans = fm // fn // fmn

    # print (ans)

    return ans
if __name__ == '__main__':
    # combine()
    print (combine())
    print (f.add(1,2,3))
