# -*- coding:utf-8 -*-
from socket import *
import time
import socket


def connect_server(stop_time):
    times_send = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    now = time.time()
    last = now + stop_time
    n = 0
    data = "aaaa"
    print('发送时间：%s----- ----发送的数据为%s' %(times_send, data))
    # 发送数据
    data = bytes(data, encoding="utf-8")
    ip_port = ('47.106.64.230', 9091)
    sk = socket.socket()
    sk.connect(ip_port)
    sk.sendall(data)
    while(now <= last):
        now = time.time()
        print("------现在时间：%s------" %now)
        times_rev =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        server_reply = sk.recv(1024)
        print('接受时间：%s----- ----接受到的数据为：%s' %(times_rev, server_reply))
        time.sleep(1)
        n += 1
    sk.close()
    print("关闭socket")

def runner(stop_time):

    number = 1
    # while(True):
    #     print("第：%s次发送打印任务" %i)
    #     connect_server(stop_time)
    #     i += 1
    for i in range(1):
        print("第：%s次发送任务" %number)
        connect_server(stop_time)
        number += 1
        i += 1
runner(30)








"""
def connect_server(stop_time):
    times_send = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    now = time.time()
    last = now + stop_time
    n = 0
    data = "{'token': '4a7d1ed414474e4033ac29ccb8653d9b','cmd': 1201,'data': {'id': '86111537348946189','url': ['http://img.zcool.cn/community/014c3e594f215da8012193a31deeca.png'],'copies': 1,'mode': 0,'type': 0,'level': 0,'size': 0,'side': 1,'autoscale': 1,'start_page': 1,'end_page': 11}}"
    print('发送时间：%s----- ----发送的数据为%s' %(times_send, data))
    # 发送数据
    data = bytes(data, encoding="utf-8")
    ip_port = ('192.168.100.2', 9000)
    sk = socket.socket()
    sk.connect(ip_port)
    sk.sendall(data)
    while(now <= last):
        now = time.time()
        print("------现在时间：%s------" %now)
        times_rev =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        server_reply = sk.recv(1024)
        print('接受时间：%s----- ----接受到的数据为：%s' %(times_rev, server_reply))
        time.sleep(1)
        n += 1
    sk.close()
    print("关闭socket")

def runner(stop_time):

    number = 1
    # while(True):
    #     print("第：%s次发送打印任务" %i)
    #     connect_server(stop_time)
    #     i += 1
    for i in range(1):
        print("第：%s次发送任务" %number)
        connect_server(stop_time)
        number += 1
        i += 1
runner(30)

"""

