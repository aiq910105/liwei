# * conding:utf-8 *
# Author : 29462
# Create_Time 2018/7/31: 19:02
# import threading
# import time
#
# num = 1000
#
# L = threading.Lock
# l = threading.RLock  # 解决死锁的方法， 使用递归锁
# def add():
#     global num  # 获取全局变量num
#     L.acquire()  # 加锁
#     for i in range(10):
#         num -= 1
#         time.sleep(1)
#     L.release()  # 解锁
#
#
# j = 0
# threading_list = []
#
# while(j<100):
#     j += 1
#     t = threading.Thread(target=add)
#     t.start()
#     threading_list.append(t)
#
# for t in threading_list:
#     t.join()
#
# print(num)
# 同一时间只能有5个线程并发进行，等待别的线程结束后，其它的线程才能开启
# threading.BoundedSemaphore(5)

# 信号量是用来控制线程并发数的

# 队列

import queue
d = queue.Queue(10)
List = []
List.append(d.put('liwei'))
List.append(d.put('carry'))
List.append(d.put('3'))
List.append(d.put('4'))
List.append(d.put('5'))
List.append(d.put('6'))

# 先进先出
i = 0
while(i<len(List)):
    i += 1
    print(d.get())
