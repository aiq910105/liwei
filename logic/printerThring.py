# -*- coding:utf-8 -*-
"""
__Date__ = '2018/8/27'
__author__ = '29462'
__filename__ = 'Soket_server'
"""
from urllib import request, parse
from urllib.error import URLError
import requests
import threading
import time
import datetime


def stamp_to_time(str_time):
    timeArray = time.localtime(str_time)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S:%m", timeArray)
    return otherStyleTime


def API():
    sends = requests.post("http://47.106.64.230/api/user/login",data={"user_account":"13662260643","user_pass":"tya123456"})
    request = sends.json()
    print("接口返回的线程", request["msg"])
thrid = []
for i in range(10):
    t = threading.Thread(target=API)
    print("线程开始时间：%s---------线程编号%s" %(datetime.datetime.now(), t.getName()))
    t.start()
    thrid.append(t)
    print("线程是否结束", t.is_alive())
thrid1 = thrid
for i in thrid:
    print("线程号", i)
    if i.is_alive() == True:
        thrid.pop(i)


