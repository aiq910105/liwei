# -*- coding:utf-8 -*-
"""
__Date__ = '2018/8/27'
__author__ = '29462'
__filename__ = 'Soket_server'
"""
import time


class one():
    def login(self, func):
        def index():
            print(time.time())
            func()
            print(time.time())
        return index()

    @login
    def hello(self):
        print("说ok")





