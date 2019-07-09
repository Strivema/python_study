# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2019/7/9 11:43 PM
# @Software: PyCharm
def main_dict():
    score = {'ray':20,'ma':21,'fei':22}
    print(score['ray'])

    score['ray'] = 22
    score.update(li=23,wang=29)


    print (score)
    print (score.get('li'))
    print (score.popitem())
    print (score.popitem())
    print (score.pop('ma'))
    print (score)
    score.clear()
    print (score)
if __name__ == '__main__':
    main_dict()