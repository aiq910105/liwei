# * conding:utf-8 *
# Author : 29462
# Create_Time 2018/8/8: 17:24
from urllib import request, parse
from urllib.error import URLError
import requests
import threading
import time
import datetime


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

def stamp_to_time(str_time):
    timeArray = time.localtime(str_time)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S:%m", timeArray)
    return otherStyleTime



def Login():  # 定义接口函数
    # 实例化接口对象
    # try:
    # http: // dev - open.yinmei.me / Content / Upload / HtmlLocal / test.html
    login = postRequest('http://120.79.102.3:8080/api/AddPrintTask', values={"order_from": "2", "order_id": "","printer_code":"181729999AL",
            'data': '{"tp":102,"id":"123456789","url":"http://120.79.102.3:8080/html/111.html"}',
            "order_timeout": "180", "sign": "1"  },interface_name="1.login")
    login.values
    return login.post()
    # except Exception as e:
    #     print(e)


def run():
    Thring_flag = True  # 线程还没结束

    try:
        i = 0
        tasks = []  # 任务列表
        # 线程数
        task_number = 1
        start = time.time()
        # print("开始时间", start)
        print("开始时间", stamp_to_time(start))
        while i < task_number:
            i += 1
            t = threading.Thread(target=Login)
            tasks.append(t)  # 加入线程池，按需使用
            t.start()  # 多线程并发
            print("线程号为：", t.getName())
            time.sleep(2.5)
        t.join()
        # 轮询线程运行完成
        while(Thring_flag == True):
            Thring = []
            for i in tasks:
                # print(i.isAlive())
                Thring.append(i.isAlive())
            # print("线程是否结束", Thring)
            if True in Thring:
                continue
            else:
                Thring_flag == False
                break
        end = time.time()
        # print("结束时间", end)
        print("结束时间", stamp_to_time(end))
        # spend_Time = stamp_to_time(start) - stamp_to_time(end)
        spend_Time = end - start
        print('共计花费时间', spend_Time)

    except Exception as e:
        print("Erro", e)

run()



