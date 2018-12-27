# * conding:utf-8 *
# Author : 29462
# Create_Time 2018/7/31: 15:18

import requests
import time


def Pinter():
    times = time.time()
    data ={
        "app_id":"055d92d0b07c4de0954b00",
        "access_token":"ae32dd5270cb4fcbad78fc7ffb1df937",
        "merchant_code":"tm9k0",
        "printer_codes":"18160956AD",
        "copies":"1",
        "bill_no":times,
        "bill_type":3,
        "template_id":"",
        "bill_content":'{ 	"type": "1", 	"maxcount": "0", 	"p1_num": [{ 		"num": "**5", 		"p1": "单选 ", 		"n": 1, 		"combinat": "005 015 025 035 045 055 065 075 085 095 105 115" 	}], 	"p2_1": "121515123", 	"p2_2": "20171116", 	"p2_3": "2017\/11\/16", 	"p2_4": "16502100", 	"p2_5": "015775", 	"p2_6": "2017\/12\/29", 	"p2_7": "13:48:50", 	"p2_8": "￥10", 	"p3_0": "100.1", 	"p3_1": "www.bwlc.net", 	"p3_2": "6170-046178049-120667", 	"p3_3": "HT2G9T-K24CNS-MQL1YJ-CLY5QD-GB84Q", 	"p3_4": "012345678912345678", "p3_5": 2, "p4_1": 2, "p4_2": "满 20 元 扫 码 摇 大 奖\n映美云打印蒸蒸日上", "p4_3": "012345678912345678" }',
        "sign":""
    }
    result = requests.post("http://bgps.yinmei.me:8082/mcp/sys/print", params=data)
    print(result.json())

def Printer_Status():
    data = {
        "app_id": "055d92d0b07c4de0954b00",
        "access_token": "ae32dd5270cb4fcbad78fc7ffb1df937",
        "printer_codes": "18160956AD",
    }
    result = requests.post("http://bgps.yinmei.me:8082/mcp/sys/GetPrintStatus", params=data)
    result_Date = result.json()
    # print(result_Date)
    result_Date = int(result_Date['data'])
    return result_Date


def If_Printer(number,Time):
    for i in range(number):
        print("-----------次数:%s--------------" %(i+1))
        n  = Printer_Status()
        if n == 0:
            Pinter()
        else:
            print("打印机忙碌中，状态值为：",n)
        time.sleep(Time)


If_Printer(50,3)

# print(Printer_Status())