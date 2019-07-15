# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time: 2019/7/15 20:19
# @Software: PyCharm
import builtwith
import ssl
import whois
from urllib import robotparser

ssl._create_default_https_context = ssl._create_unverified_context
print(builtwith.parse('https://www.jianshu.com/'))
# print(whois('baidu.com'))
