# * conding:utf-8 *
"""
__Date__ = '2018/8/27'
__author__ = '29462'
__filename__ = 'Soket_server'
"""
from socket import *
import time
import socket
import threading


arr = []

def connect_server():
    # for i in range(200000, 201000, 1):
    #     arr.append(i)
    data ='{"tp": 101,"did":1}'
    print("发送的数据--》",data)
    data = bytes(data, encoding="utf-8")
    ip_port = ('47.106.64.230', 9509)
    sk = socket.socket()
    sk.connect(ip_port)
    sk.sendall(data)
    server_reply = sk.recv(1024)
    print("接收到的数据--》",server_reply)
    sk.close()




def keep_heart(sn):
    data = '{"tp": 100,"did":"%s"}' %sn
    data = bytes(data, encoding="utf-8")
    ip_port = ('47.106.64.230', 9509)
    sk = socket.socket()
    sk.connect(ip_port)
    sk.sendall(data)
    server_reply = sk.recv(1024)
    print(server_reply)
    # time.sleep(5)
    # while True:
    #     sk.sendall(data)
    #     server_reply = sk.recv(1024)
    #     print(server_reply)
    #     time.sleep(10)
    # print("----------")
    # sk.close()

def heart_thring():
    try:
        k = 1
        tasks = []  # 任务列表
        # 线程数
        task_number = 10000
        sn = [x for x in range(100000, 101000, 1)]
        # sn = tuple(sn)
        # 循环保持心跳
        while  True:
            print("第【%s】次保持心跳" %k)
            k += 1
            i = 0
        # 启动全部线程
            while i < task_number:
                i += 1
                # print(sn[i])
                t = threading.Thread(target=keep_heart(sn[i]))
                tasks.append(t)  # 加入线程池，按需使用
                t.start()  # 多线程并发
                print("线程号为：", t.getName())
            # t.join()
            print("----------")
            time.sleep(10)
    except Exception as e:
        print("Erro", e)


# heart_thring()
connect_server()
