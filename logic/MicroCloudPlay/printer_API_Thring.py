# * conding:utf-8 *
# Author : 29462
# Create_Time 2018/7/31: 15:18

import requests
import time
import threading


def Pinter():
    times = time.time()
    data ={
        "app_id":"055d92d0b07c4de0954b00",
        "access_token":"ae32dd5270cb4fcbad78fc7ffb1df937",
        "merchant_code":"tm9k0",
        "printer_codes":"18160958AD",
        "copies":"1",
        "bill_no":times,
        "bill_type":3,
        "bill_content":'{ 	"type": "1", 	"maxcount": "0", 	"p1_num": [{ 		"num": "**5", 		"p1": "单选 ", 		"n": 1, 		"combinat": "005 015 025 035 045 055 065 075 085 095 105 115" 	}], 	"p2_1": "121515123", 	"p2_2": "20171116", 	"p2_3": "2017\/11\/16", 	"p2_4": "16502100", 	"p2_5": "015775", 	"p2_6": "2017\/12\/29", 	"p2_7": "13:48:50", 	"p2_8": "￥10", 	"p3_0": "100.1", 	"p3_1": "www.bwlc.net", 	"p3_2": "6170-046178049-120667", 	"p3_3": "HT2G9T-K24CNS-MQL1YJ-CLY5QD-GB84Q", 	"p3_4": "012345678912345678", "p3_5": 2, "p4_1": 2, "p4_2": "满 20 元 扫 码 摇 大 奖\n映美云打印蒸蒸日上", "p4_3": "012345678912345678" }',
        "sign":""
    }
    result = requests.post("http://bgps.yinmei.me:8082/mcp/sys/print", params=data)
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
