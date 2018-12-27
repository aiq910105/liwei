# * coding:utf-8 *
# Author : 29462
# Create_Time 2018/8/8: 17:24
from urllib import request, parse
from urllib.error import URLError
import requests
import threading
import time

def Login():
        result = requests.post('https://m.chaohaigou.com/app')
        print(result.url)
        send = result.request
        print(send)

Thring_flag = True  # 线程还没结束

try:
    i = 0
    tasks = []  # 任务列表
    task_number = 50
    start = time.time()
    print("开始时间", start)
    while i < task_number:
        i += 1
        t = threading.Thread(target=Login)
        tasks.append(t)  # 加入线程池，按需使用
        t.start()  # 多线程并发
        print("线程号为：", t.getName())
        # time.sleep(0.2)
    t.join()
    while(Thring_flag == True):
        Thring = []
        for i in tasks:
            # print(i.isAlive())
            Thring.append(i.isAlive())
        # print("线程是否结束", Thring)
        if True in Thring:
            continue
        else:
            Thring_flag==False
            break

    end = time.time()
    print("结束时间", start)
    spend_Time = end - start
    print('共计花费时间', spend_Time)

except Exception as e:
    print(e)

