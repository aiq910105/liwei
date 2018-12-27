# * conding:utf-8 *
# Author : 29462
# Create_Time 2018/8/6: 11:21
#
import requests
import json
def login():
    result = requests.post("http://cloud_app.yinmei.me//api/tmuser/saveInfo", params={
    "info": '{"姓名": "金桥"}',
    "printer_code": '18220324AY',
    "print_data": '{"d_P0": "金桥"}',
    "template_id": '180809183322148BAA7',
    }

    )
    print("拼接的URL", result)
    send = result.text
    print(send)
    # if send["code"] != 200:
    #     print(send["msg"])
    #     print(send)
    # else:
    #     print(result.json())


if __name__ == '__main__':
    login()
# import time
# import threading
#
# i = 0
# j = 0
# def add():
#     for i in range(1000000):
#         i += 1
#         time.sleep(0.0000000002)
#         print("le")
#
#
# while(j<100):
#     j += 1
#     k = threading.Thread(target=add)
#     k.start()
#     print(k)


