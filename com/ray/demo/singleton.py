# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time: 2019/7/13 11:24
# @Software: PyCharm
from functools import wraps


def singleton(cls):
    instance = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper


@singleton
class Student():
    pass
