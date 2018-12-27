# * conding:utf-8 *
# Author : 29462
# Create_Time 2018/8/8: 17:24
from urllib import request, parse
from urllib.error import URLError
import requests
import threading
import time


class postRequest():
    def __init__(self, url, values, interface_name):
        self.url = url
        self.values = values
        self.interface_name = interface_name

    def post(self):
        parms = self.values
        # querystring = parse.urlencode(parms)
        try:
            result = requests.post(self.url, parms)
            print(result.url)
            send = result.json()
            print(send)
            # if send['code'] == 400:
            #     return 0
            # else:
            #     return 1
        except URLError as e:
            print(e)


def log(s):
    print(s)

def Login():  # 定义接口函数
    # 实例化接口对象
    # try:
    login = postRequest('http://120.79.102.3:8080/api/AddPrintTask', values={"order_from": "2", "order_id": "",
            "printer_code": "zhouming123", "data": "{tp:102,url:http://yinmei.me}", "order_timeout": "60", "sign": "1"},
                        interface_name="1.login")
    return login.post()
    # except Exception as e:
    #     print(e)

Thring_flag = True  # 线程还没结束

try:
    i = 0
    tasks = []  # 任务列表
    task_number = 1
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