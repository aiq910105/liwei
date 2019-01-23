# * conding:utf-8 *
# Author : leo
# Create_Time  2019/1/23 17:04

import pymysql
import time

class Datebase_select():
    def __init__(self):
        pass
    def OrderDate(self, printer_Code, StartTime, EndTime):
        conn = pymysql.connect(host="47.106.85.252", port=3306, user="root", passwd="123456", db="mcp_test",
                               charset="utf8")
        cur = conn.cursor()
        # sql = ("select * from mcp_order_printer where printer_code =%s and created_on BETWEEN %s and %s")
        reCount = cur.execute(
            "select * from mcp_order_printer where printer_code =%s and created_on BETWEEN %s and  %s",
            (printer_Code, StartTime, EndTime))
        sql_data = cur.fetchall()
        # return sql_data
        if sql_data:
            return sql_data
        else:
            return '没数据'
        cur.close()
        conn.close()

    def search_printer(self, printer_Code):
        # sqlArr = None
        conn = pymysql.connect(host="47.106.85.252", port=3306, user="root", passwd="123456", db="mcp_test",
                               charset="utf8")
        cur = conn.cursor()
        # x = request.GET.get("printer", "")
        sql = ("select * from mcp_equipment where equipment_code = %s")
        reCount = cur.execute(sql, printer_Code)
        sql_data = cur.fetchone()
        if sql_data != None:
            return sql_data
        else:
            return None
        cur.close()
        conn.close()


# datas = Datebase_select.search_printer('', '18340058AL')
# print(Datebase_select().search_printer('18340058AL'))
