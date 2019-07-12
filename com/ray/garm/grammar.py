# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time: 2019/7/12 13:53
# @Software: PyCharm
import heapq
import itertools
from collections import Counter


def main():
    prices = {'AAPL': 191.88,
              'GOOG': 1186.96,
              'IBM': 149.24,
              'ORCL': 48.44,
              'ACN': 166.89,
              'FB': 208.09,
              'SYMC': 21.29}
    price = {key: value for key, value in prices.items() if value > 200}
    print(price)


def heap_list():
    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    print(heapq.nlargest(3, list1))
    print(heapq.nsmallest(3, list1))


def iter_list():
    print(itertools.permutations('ABCD'))
    itertools.combinations('ABCDE', 3)
    itertools.product('ABCD', '123')


def find_list():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    count = Counter(words)
    print(count.most_common(3))
    print(count.items())
    print(count.get('look'))
    print(count.values())


if __name__ == '__main__':
    # heap_list()
    # iter_list()

    find_list()
