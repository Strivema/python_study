# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time: 2019/7/15 17:11
# @Software: PyCharm
import pymysql

def main():
    con = pymysql.connect(host='10.10.14.41', port=3306,
                          database='chinaentropy',
                          charset='utf8',
                          user='root',
                          password='Weiwei@2018')
    try:
        with con.cursor() as cursor:
            cursor.execute('select * from t_pstype')
            result = cursor.fetchall()
            print(result)
    finally:
        con.close()


if __name__ == '__main__':
    main()
