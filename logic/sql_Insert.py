# * conding:utf-8 *
# Author : 29462
# Create_Time 2018/7/31: 15:18
import pymysql
import time
import threading
import datetime



def demo(id):
    conn = pymysql.connect(host="121.40.151.135", port=3306, user="prt_dever", passwd="dbdatadev",
                           db="ps_pressure_test",
                           charset="utf8")
    cur = conn.cursor()
    # cur.execute("show variables like '%max_connections%';")
    sql = ("INSERT INTO mcp_callbackrecord VALUE(%s,'','','18340058AL','1','2018--11--26 14:40:19','2018--11--26 14:40:19') ")
    cur.execute(sql, id)
    conn.commit()


    cur.close()
    conn.close()





def run(number, id):
    Thring_flag = True  # 线程还没结束
    Thring_number = []
    for n in range(number):
        Thring_number.append(id + n + 1)
    # print("产生的" ,Thring_number)
    try:
        i = 0
        tasks = []  # 任务列表
        # 线程数
        task_number = number
        start_Time = time.time()
        start_local = time.localtime(start_Time)
        print("结束时间", time.strftime("%Y--%m--%d %H:%M:%S", start_local))
        # print("开始时间", start_Time)
        # while i< task_number:
        #     # print("运行时", Thring_number[i])
        #     demo(Thring_number[i])
        #     i += 1

        while i < task_number:
            # print("拿到的ID", Thring_number[i])
            t = threading.Thread(target=demo, args=(Thring_number[i],))
            tasks.append(t)  # 加入线程池，按需使用
            ThringStart_Time = time.time()
            t.start()  # 多线程并发
            print("线程号为：", t.getName(), "线程开始运行时间", ThringStart_Time)
            i += 1
        t.join()

        End_Time = time.time()
        # print("---------", End_Time)
        End_local = time.localtime(End_Time)
        print("结束时间", time.strftime("%Y--%m--%d %H:%M:%S", End_local))
        spend_Time = End_Time - start_Time
        print('共计花费时间', round(spend_Time,8))

    except Exception as e:
        print("Erro", e)

run(1000,18578401)

def count(runNuber, number,sleepTime):
    for i in range(runNuber):
        print("###############第%s次运行###################" %(i+1))
        run(number)
        time.sleep(sleepTime)

