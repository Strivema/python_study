# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time: 2019/7/11 18:40
# @Software: PyCharm
import json


def main():
    f = None
    try:
        f = open('hello.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('file not in memory')
    except LookupError:
        print('unknown encoding')
    except UnicodeDecodeError:
        print('error')
    finally:
        if f:
            f.close()


def main_json():
    mydict = {
        'name': 'ray',
        'age': 17,
        'qq': 95722658,
        'friends': ['li', 'yuan'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main_json()
