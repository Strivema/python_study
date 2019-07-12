# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time: 2019/7/12 19:31
# @Software: PyCharm
def main():
    items = list(map(int, input().split()))
    size = len(items)
    over, par = {}, {}
    over[size - 1] = par[size - 1] = items[size - 1]
    for i in range(size - 2, -1, -1):
        par[i] = max(items[i], par[i + 1] + items[i])
        over[i] = max(par[i], over[i + 1])
    print(over[0])


if __name__ == '__main__':
    main()
