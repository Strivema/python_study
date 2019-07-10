# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2019/7/10 11:36 PM
# @Software: PyCharm
class Person(object):
    __slots__ = ('_name', '_age', '_gender')
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('ray', 12)
    person.play()
    person.age = 21
    person.play()
    person._gender ='man'
if __name__ == '__main__':
    main()