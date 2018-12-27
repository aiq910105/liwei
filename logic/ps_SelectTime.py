# * coding:utf-8 *
# Author : 29462
# Create_Time 2018/8/10: 9:29
import pymysql
import time
import datetime
import logging


# 统计打印机从发送任务到打印完成的时间
def Printer_Time(Printer_Code, Time):
    """"
    Printer_Code 打印机编号
    Time 从发送任务到打印机打印出来且上报给服务器的时间
    """
    conn = pymysql.connect(host='120.79.101.183', user='ymuser', passwd='yingmei2018', db='mcp_tcp')
    cur = conn.cursor()
    # 查询
    # received_time 9    created_on 10   modified_on 11
    # sql = ("select * from mcp_printer_task t where printer_code = %s  and created_on >='2018-10-11 19:24:00'", printer)
    reCount = cur.execute("select * from mcp_printer_task t where printer_code = %s  and created_on  between '2018-10-18 20:45:00' and ' 2018-10-19 20:22:05'", Printer_Code)  # 返回受影响的行数
    print('查询到的总条数',reCount)
    count = 0
    data = cur.fetchall()  # 返回数据,返回的是tuple类型
    sum = 0
    for i in data:
        received_time = i[9]
        created_on = i[10]
        modified_on = i[11]
        # 把datetime.datetime格式转化为字符串
        received_time = str(received_time)
        created_on = str(created_on)
        modified_on = str(modified_on)
        count += 1
        # print("运行到%s条数据有问题，订单号为：%s"%(count, i[1]))
        # 转换为时间戳格式
        if received_time != None:
            received_time = string2timestamp(received_time)
        if modified_on != None:
            modified_on = string2timestamp(modified_on)
        Time_Difference = modified_on - received_time
        if Time_Difference >= Time:
            sum +=1
            print('打印完成时间:',i[11],'打印发送时间:',i[10],'打印机编号：',i[2],'订单id:',i[1],'从发送任务到打印完成的时间', Time_Difference)
    print('打印机超过%s 秒未打印的条数为%s：' % (Time, sum))

    cur.close()
    conn.close()


def string2timestamp(strValue):
    try:
        d = datetime.datetime.strptime(strValue, "%Y-%m-%d %H:%M:%S")
        t = d.timetuple()
        timeStamp = int(time.mktime(t))
        timeStamp = float(str(timeStamp) + str("%06d" % d.microsecond)) / 1000000
        return timeStamp
    except ValueError as e:
        print(e)
        d = datetime.datetime.strptime(strValue, "%Y-%m-%d %H:%M:%S")
        t = d.timetuple()
        timeStamp = int(time.mktime(t))
        timeStamp = float(str(timeStamp) + str("%06d" % d.microsecond)) / 1000000
        return timeStamp

def Order_Status(Printer_Code):
    """"
    Printer_Code 打印机编号
    Time 从发送任务到打印机打印出来且上报给服务器的时间
    """
    conn = pymysql.connect(host='120.79.101.183', user='ymuser', passwd='yingmei2018', db='mcp_tcp')
    cur = conn.cursor()
    # 查询
    # received_time 9    created_on 10   modified_on 11
    # sql = ("select * from mcp_printer_task t where printer_code = %s  and created_on >='2018-10-11 19:24:00'", printer)
    reCount = cur.execute("select * from mcp_printer_task t where printer_code = %s  and created_on  between '2018-10-18 20:45:00' and ' 2018-10-19 20:22:05'", Printer_Code)  # 返回受影响的行数
    print('查询到的总条数',reCount)
    data = cur.fetchall()  # 返回数据,返回的是tuple类型
    sum = 0
    count_abnormity = 0
    for i in data:
        if i[3] == 1:
            sum += 1
            continue
        else:
            count_abnormity += 1
            if i[9] == None and i[3] != 100:
                print("---该订单异常，请查看-- ",'打印完成时间:', i[11], '创建打印任务时间:', i[10], '—接收时间—:', i[9] , '打印机编号：', i[2], '订单id:', i[1], '打印状态', i[3] )
                continue
            else:
                print('打印完成时间:', i[11], '创建打印任务时间:', i[10], '—接收时间—:', i[9] , '打印机编号：', i[2], '订单id:', i[1], '打印状态', i[3])
                continue
    if reCount == sum:
        print("全部打印成功，没有异常打印状态")
    else:
        print("打印失败条数：%s" % count_abnormity)

    cur.close()
    conn.close()


def Weiyunda_SelfStatus(Printer_Code):
    """"
    Printer_Code 打印机编号
    Time 从发送任务到打印机打印出来且上报给服务器的时间
    """
    conn = pymysql.connect(host='47.106.85.252', user='root', passwd='123456', db='mcp_devyinmei')
    cur = conn.cursor()
    # 查询
    # received_time 9    created_on 10   modified_on 11
    sql = ("SELECT * FROM mcp_order_printer WHERE printer_code = %s and created_on between '2018-10-18 20:45:00' and ' 2018-10-19 20:22:05'")
    # reCount = cur.execute("SELECT * FROM mcp_order_printer WHERE printer_code = %s ORDER BY created_on DESC", Printer_Code)  # 查看订单状态
    reCount = cur.execute(sql, Printer_Code)
    print('查询到的总条数',reCount)
    data = cur.fetchall()  # 返回数据,返回的是tuple类型
    status_ok = 0
    status_fail = 0
    for i in data:
       if i[4] == 1:
           status_ok += 1
           continue
       else:
           print("自己的服务器的异常状态为：", i[4])
           status_fail += 1
           continue
    print("成功条数为：%s————打印失败条数为%s" % (status_ok, status_fail))
    cur.close()
    conn.close()


def Weiyunda_ClineStatus(Printer_Code):
    """"
    Printer_Code 打印机编号
    Time 从发送任务到打印机打印出来且上报给服务器的时间
    """
    conn = pymysql.connect(host='47.106.85.252', user='root', passwd='123456', db='mcp_devyinmei')
    cur = conn.cursor()
    # 查询
    # received_time 9    created_on 10   modified_on 11
    sql = ("select * from mcp_order where order_id in(select order_id from mcp_order_printer where printer_code= %s and created_on between '2018-10-18 20:45:00' and ' 2018-10-19 20:22:05')")
    # reCount = cur.execute("SELECT * FROM mcp_order_printer WHERE printer_code = %s ORDER BY created_on DESC", Printer_Code)  # 查看订单状态
    reCount = cur.execute(sql, Printer_Code)
    print('查询到的总条数', reCount)
    data = cur.fetchall()  # 返回数据,返回的是tuple类型
    status_ok = 0
    status_fail = 0
    for i in data:
       if i[11] == 10001:
           status_ok += 1
           continue
       else:
           print('客户调用的异常状态码为: ', i[11])
           status_fail += 1
           continue
    print("成功条数为：%s————打印失败条数为%s" % (status_ok, status_fail))


    cur.close()
    conn.close()



# Printer_Time('17320204WV', 15)
Order_Status('17080253UJ')
Weiyunda_SelfStatus('17320204WV') #查询微云打程序打印状态
Weiyunda_ClineStatus('17320204WV') #查询微云打回调给用户状态