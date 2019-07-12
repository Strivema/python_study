# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time: 2019/7/12 16:01
# @Software: PyCharm
'''
\公鸡5元一只 母鸡3元一只 小鸡1元三只
 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
'''


def main_easy():
    for i in range(20):
        for j in range(33):
            m = 100 - i - j
            if 5 * i + 3 * j + m // 3 == 100 and m % 3 == 0:
                print(i, j, m)


def main_part():
    fish = 6
    while True:
        total = fish
        enough = True
        for i in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 5


if __name__ == '__main__':
    # main_easy()

    main_part()