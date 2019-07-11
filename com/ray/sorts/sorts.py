# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2019/7/11 11:10 PM
# @Software: PyCharm
def select_sort(origin_items, comp=lambda x, y: x < y):
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(origin_items,comp = lambda x,y:x<y):
    item =  origin_items[:]



if __name__ == '__main__':
    t1 = [2, 7, 6, 3, 5]
    print(select_sort(t1))
