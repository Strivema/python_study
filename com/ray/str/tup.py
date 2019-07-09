def main():
    t = ('1','ray',True,'ok')
    print (t)


    for i in t:
        print (i)
    person = list(t)
    print (person)
    # person[0] = '2'
    # persion[1] = 'jack'
    # print person
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print (fruits_tuple)

def main_set():
    set1 = {1, 2, 3, 3, 3, 2}
    print (set1)
    print (len(set1))
    set1.add(4)
    set1.add(5)
    print (set1)
    set2 = range(1,10)
    print (set2)
    # set2.update([11,12])
    print (set2)
    # set2.discard(5)

    # if 4 in set2:
    #     set2.remove(4)
    # print(set2)

    for elem in set2:
        print(elem ** 2)
    print()

    # set3 = set((1, 2, 3, 3, 2, 1))
    # print(set3.pop())

    print(set1 & set2)
    # print(set1.intersection(set2))
    print(set1 | set2)
    # print(set1.union(set2))
    print(set1 - set2)
    # print(set1.difference(set2))
    print(set1 ^ set2)
    # print(set1.symmetric_difference(set2))

    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set1 >= set2)
    # print(set1.issuperset(set2))
    print(set1 >= set3)

if __name__ == '__main__':
    main_set()