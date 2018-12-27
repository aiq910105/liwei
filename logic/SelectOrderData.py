# * conding:utf-8 *
# Author : 29462
# Create_Time 2018/7/31: 15:18
import pymysql
import time




def OrderDate(printer_Code, StartTime, EndTime):
    conn = pymysql.connect(host="47.106.85.252", port=3306, user="root", passwd="123456", db="mcp_test",
                           charset="utf8")
    cur = conn.cursor()
    # sql = ("select * from mcp_order_printer where printer_code =%s and created_on BETWEEN %s and %s")
    reCount = cur.execute("select * from mcp_order_printer where printer_code =%s and created_on BETWEEN %s and  %s", (printer_Code, StartTime, EndTime))
    sql_data =cur.fetchall()
    if not sql_date:
    # if sql_data != None:
        # print(sql_data)
        return sql_data
        # for i in sql_data:
        #     print(i)
    else:
        return None
    cur.close()
    conn.close()





