# * conding:utf-8 *
# Author : 29462
# Create_Time 2018/7/31: 15:18

import requests
import time
import threading


def Pinter():
    times = time.time()
    data ={
        "app_id":"11111111111111111111111111111111",
        "access_token":"11111111111111111111111111111111",

    }
    result = requests.post("http://cloudapi.yinmei.me:81/mcp/app/add", params=data)
    return result.json()

def run(number):
    try:
        i = 0
        tasks = []  # 任务列表
        # 线程数
        start_Time = time.time()
        print("整体开始时间", start_Time)
        while i < number:
            i += 1
            t = threading.Thread(target=Pinter)
            tasks.append(t)  # 加入线程池，按需使用
            ThringStart_Time = time.time()
            start_Time1 = time.time()
            t.start()  # 多线程并发
            print("线程号为：", t.getName(), "线程开始运行时间", ThringStart_Time)
        t.join()
        End_Time = time.time()
        print("结束时间", End_Time)
        spend_Time = End_Time - start_Time
        print('共计花费时间%s秒' %round(spend_Time,8))
    except Exception as e:
        print("Erro", e)

run(1)
