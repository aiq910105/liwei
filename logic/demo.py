# * conding:utf-8 *
# Author : 29462
# Create_Time 2018/7/31: 15:18
import pymysql
import time




def search_printer(printer_Code):
    # sqlArr = None
    conn = pymysql.connect(host="47.106.85.252", port=3306, user="root", passwd="123456", db="mcp_test",
                           charset="utf8")
    cur = conn.cursor()
    # x = request.GET.get("printer", "")
    sql = ("select * from mcp_equipment where equipment_code = %s")
    reCount = cur.execute(sql, printer_Code)
    sql_data =cur.fetchone()
    if sql_data != None:
        sql_data = list(sql_data)
        return sql_data
    else:
        return None
    cur.close()
    conn.close()


search_printer("18340058AL")

def login(printer_code):
    data = search_printer(printer_code)
    print(type(data))

    if data:
        print("YES")
    else:
        print("NO")

login("18340058AL")