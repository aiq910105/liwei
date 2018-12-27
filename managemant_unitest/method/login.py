# * coding:utf-8 *
# Author : 29462
# Create_Time 2018/8/3: 19:41
from managemant_unitest.config.config_requestUrl import Url
import requests
import logging





class Login:
    def __init__(self, url):
        self.url = url

    def login(self, params):
        url = Url.url()
        # {"user_pass": "tya123456", "user_account": 13662260643}
        result = requests.get(self.url, params)
        send = result.json()
        if  send['code']== 200:
            # print([1, send['data']['user_token']])
            return [1, send['data']['user_token']]
        else:
            print("___________")
            return [0, send['msg']]


def login_result(params):
    URL = Url.url()
    method_login = Login(URL)
    S = method_login.login(params)
    # print(S)
    return S

def login_Success():
    login_result({"user_pass": "tya123456", "user_account": 13662260643})

def login_Fail_usernameIsNull():
    login_result({"user_pass": "tya123456", "user_account": ''})

