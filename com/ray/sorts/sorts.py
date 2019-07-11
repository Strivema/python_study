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


def bubble_sort(origin_items, comp=lambda x, y: x < y):
    item = origin_items[:]
    for i in range(len(item) - 1):
        temp = False
        for j in range(i, len(item) - 1 - i):
            if comp(item[j - 1], item[j]):
                item[j], item[j - 1] = item[j - 1], item[j]
                temp = True
        if temp:
            temp = False
            for j in range(len(item) - 2 - i, i, -1):
                if comp(item[j - 1], item[j]):
                    item[j], item[j - 1] = item[j - 1], item[j]
                    temp = True
        if not temp:
            break
    return item


def seq_search(items, key):
    for i in range(len(items) - 1):
        if items[i] == key:
            return i
    return -1


def seq_find(items, key):
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


if __name__ == '__main__':
    t1 = [2, 7, 6, 3, 5]
    print(select_sort(t1))
