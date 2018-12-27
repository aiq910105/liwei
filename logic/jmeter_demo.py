# * conding:utf-8 *
# Author : 29462
# Create_Time 2018/7/31: 15:18
import pymysql
import time
import threading
import datetime



def demo():
    conn = pymysql.connect(host="121.40.151.135", port=3306, user="prt_dever", passwd="dbdatadev",
                           db="ps_pressure_test",
                           charset="utf8")
    cur = conn.cursor()
    # cur.execute("show variables like '%max_connections%';")
    # sql = ("SELECT * FROM mcp_app_token WHERE app_id = '0055d92d0b07c4de0954b00' ")
    # sql = ("UPDATE mcp_app_token SET access_token = '0c1ee9f0984d74e4f8a69e0',created_on = '2018-11-22 23:27:13'WHERE app_id = '0055d92d0b07c4de0954b00'")
    # sql = ("SELECT * FROM `mcp_order_printer` WHERE printer_code='18340058AL' AND order_status IN (0,2,5,8,9,10,11,12) AND TO_SECONDS('2018-11-02 11:48:08')-TO_SECONDS(created_on)>15;")
    # sql = ("SELECT * FROM mcp_equipment WHERE equipment_code ='18340058AL'")
    # sql = ("UPDATE mcp_equipment SET var_version = '3.0.18',firmware_version = '0.0.1' WHERE equipment_code ='18340058AL'")
    # sql = ("DELETE FROM mcp_merchant_printer WHERE printer_code ='8C18D9FF1C9' AND app_id ='a5dc14cbe98d4e229e60a7c1e52b6808'")
    # sql = ("UPDATE mcp_order SET callback_status = '1' WHERE order_id = 'ea42fafd-ef38-11e8-873a-02004c4f4f50'")
    # sql = ("UPDATE mcp_order_printer SET order_status ='1' WHERE order_id = '0929eac53d860cfa49eaae5f1dac8517f5c9'")
    sql = ("UPDATE `mcp_order_printer` SET order_status=2 WHERE printer_code='18340058AL' AND order_status IN (0,2,5,8,9,10,11,12)  AND TO_SECONDS('2018/11/12 17:24:13')-TO_SECONDS(created_on)>15")
    # sql =("SELECT * FROM `mcp_order_printer` WHERE printer_code='18340058AL' AND order_status IN (0,2,5,8,9,10,11,12) AND TO_SECONDS('2018/11/12 17:24:13')-TO_SECONDS(created_on)>15;")
    # sql = ("SELECT * FROM mcp_paper_type WHERE paper_type = '1'")
    # sql = ("SELECT * FROM mcp_printer WHERE printer_code ='18340058AL'")
    # sql =("SELECT order_id,order_status FROM mcp_order_printer WHERE printer_code='18340058AL' AND order_status IN (0,2,5,8,9,10,11,12) AND created_on<'2018/11/12 17:23:58'")
    reCount = cur.execute(sql)
    cur.close()
    conn.close()

def insert(id):
    conn = pymysql.connect(host="121.40.151.135", port=3306, user="prt_dever", passwd="dbdatadev",
                           db="ps_pressure_test",
                           charset="utf8")
    cur = conn.cursor()

    reCount = cur.execute(sql)

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
            tasks.append(t)  # 加入线程池，按需使用
            ThringStart_Time = time.time()
            t.start()  # 多线程并发
            print("线程号为：", t.getName(), "线程开始运行时间", ThringStart_Time)
        t.join()
        End_Time = time.time()
        print("结束时间", End_Time)
        spend_Time = End_Time - start_Time
        print('共计花费时间', round(spend_Time,8))
    except Exception as e:
        print("Erro", e)

run(500)

def count(runNuber, number,sleepTime):
    for i in range(runNuber):
        print("--------------------第%s次运行--------------------" %(i+1))
        run(number)
        time.sleep(sleepTime)

# count(1, 800, 1)