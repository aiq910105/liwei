from django.shortcuts import render

# Create your views here.
# from logic.demo import *
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
# from logic.SelectOrderData import *
from logic.DB_Select import *
import time

# def hello(request):
#     return HttpResponse("Hello world ! ")

def index(request):
        return  render(request, 'h5/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        data =Datebase_select().search_printer(username)
        # data = search_printer(username)
        # 判断数组是否有元素，data（有证明sql查询到数据了）
        if data:
            return render(request, 'h5/regist1.html', {'data': data})
        else:
            return HttpResponse("未输入打印机编号或打印机编号不存在")
    else:
        return render(request, 'h5/regist1.html', {'erro': "没请求"})


def selectOrder(request):
    if request.method == 'POST':
        StratData = request.POST.get('strat_data')
        StratTime = request.POST.get('strat_time')
        EndDate = request.POST.get('end_data')
        EndTime = request.POST.get('end_time')
        PinterCode = request.POST.get("printer_code")
        Strat = StratData + " " + StratTime
        End = EndDate + " " + EndTime
        # Order_Date = OrderDate(PinterCode,Strat,End)
        Order_Date = Datebase_select().OrderDate(PinterCode,Strat,End)
        #如果有数据
        if Order_Date:
            return render(request, 'h5/printer_order.html', {'Order_Date': Order_Date})
        else:
            return HttpResponse("查询不到数据")
    else:
        return render(request, 'h5/printer_order.html', {'erro': "没请求"})

def Chnck_Code(request):
    pass

