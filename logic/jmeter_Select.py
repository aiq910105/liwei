# * conding:utf-8 *
# Author : 29462
# Create_Time 2018/7/31: 15:18
import pymysql
import time
import threading



def demo():
    conn = pymysql.connect(host="121.40.151.135", port=3306, user="prt_dever", passwd="dbdatadev",
                           db="ps_pressure_test",
                           charset="utf8")
    cur = conn.cursor()

    sql = ("SELECT * FROM mcp_app_token WHERE app_id = '0055d92d0b07c4de0954b00' ")
    # sql = ("UPDATE mcp_app_token SET access_token = '0c1ee9f0984d74e4f8a69e0',created_on = '2018-11-22 23:27:13'WHERE app_id = '0055d92d0b07c4de0954b00'")
    # sql = ("SELECT * FROM `mcp_order_printer` WHERE printer_code='18340058AL' AND order_status IN (0,2,5,8,9,10,11,12) AND TO_SECONDS('2018-11-02 11:48:08')-TO_SECONDS(created_on)>15;")
    reCount = cur.execute(sql)
    data = cur.fetchall()
    # print("1----------", data)
    cur.close()
    conn.close()





def run(number):
    Thring_flag = True  # 线程还没结束

    try:
        i = 0
        tasks = []  # 任务列表
        # 线程数
        task_number = number
        start_Time = time.time()
        print("开始时间", start_Time)
        while i < task_number:
            i += 1
            t = threading.Thread(target=demo)
            tasks.append(t)  # 加入线程池
            ThringStart_Time = time.time()
            # print("开始时间", start_Time)
            t.start()  # 多线程并发
            print("线程号为：", t.getName(), "线程开始运行时间", ThringStart_Time)
        t.join() #join()方法等待线程完成
        End_Time = time.time()
        print("结束时间", End_Time)
        spend_Time = End_Time - start_Time
        print('共计花费时间', spend_Time)

    except Exception as e:
        print("Erro", e)

# run(1000)

def count(runNuber, number,sleepTime):
    for i in range(runNuber):
        # print("###############第%s次运行###################" %(i+1))
        run(number)
        time.sleep(sleepTime)

count(20, 100, 1)

