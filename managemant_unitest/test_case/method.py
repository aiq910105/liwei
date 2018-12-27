# * coding:utf-8 *
# Author : 29462
# Create_Time 2018/8/6: 11:00
import requests
import json
from managemant_unitest.config.config_requestUrl import Url

class Method:
    def __init__(self, url):
        self.url = url
    def login(self):
        url = Url.url()
        # print(url)
        # print(self.url)
        sussuse = requests.get(self.url, {"user_pass": "tya123456", "user_account": 13662260643})
        send = sussuse.json()
        print(send)



