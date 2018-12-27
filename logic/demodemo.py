# * conding:utf-8 *
# Author : 29462
# Create_Time 2018/7/31: 15:18
import math
def demo(day):
    tatal = 0
    for i in range(day):
        tatal = math.pow(2, i) + tatal
        print("天数%s----金额%s" %(i, tatal))

demo(30)