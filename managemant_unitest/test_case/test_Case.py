# * coding:utf-8 *
# Author : 29462
# Create_Time 2018/8/3: 19:41
from managemant_unitest.method.login import *
import unittest


# 用例类
class Case(unittest.TestCase):

    def setUp(self):
        pass  # 用例运行前执行函数

    def test_login_success(self):
        self.assertEqual(1, login_Success()[0], "登录成功")

    def test_login_Fail1(self):
        self.assertEqual(0, login_Fail_usernameIsNull()[0], "用户名不能为空")



# if __name__ == '__main__':
#     unittest.main()


