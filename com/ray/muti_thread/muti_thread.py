# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2019/7/11 10:04 PM
# @Software: PyCharm
from random import randint
from time import time, sleep
from multiprocessing import Process
from os import getpid
from threading import Thread

# 单线程
def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))




def main():
    start = time()
    download_task('Python.pdf')
    download_task('Peking.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

def main_mut():
    start = time()
    p1 = Process(target=download_task, args=('Python.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('Peking.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))
def main_muti():
    start = time()
    t1 = Thread(target=download_task,args=('java.pdf'))
    t1.start()
    t2 = Thread(target=download_task, args=('Peking Hot.avi',))
    t2.start()

    t1.join()
    t1.join()
    end = time()
    print ('all time%.2f'%(end-start))




if __name__ == '__main__':
    # main_mut()
    main_muti()