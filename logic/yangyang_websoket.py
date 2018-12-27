# -*- coding:utf-8 -*-
from socket import *
import time
import socket

def connect_server(stop_time):
    times_send = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    now = time.time()
    last = now + stop_time
    n = 0
    data = "{'data':{'identifier':'00045fa2c693','version':'2.2.6.test'},'methodCode':1,'sequence':'9cd914077369417ba4e400fbb83a3947'}"
    print('发送时间：%s----- ----发送的数据为%s' %(times_send, data))
    # 发送数据
    data = bytes(data, encoding="utf-8")
    ip_port = ('47.91.129.200', 8989)
    sk = socket.socket()
    sk.connect(ip_port)
    sk.sendall(data)
    while(now <= last) :
        now_1 = time.time()
        times_rev =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        server_reply = sk.recv(1024)
        server_reply = server_reply.decode()
        print('接受时间：%s----- ----接受到的数据为：%s /n' %(times_rev, server_reply))
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
runner(1)