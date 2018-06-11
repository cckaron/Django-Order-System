from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from orderform.models import order
from orderform.form import OrderForm
from django.http import JsonResponse
import datetime
import xlwt
# Create your views here.

def export(request):
    if not request.user.is_authenticated:
        return redirect('/order')

    if request.method == "POST":
        date = request.POST['date']
        dateList = date.split('/')
        red = '/export/' + dateList[0] + dateList[1] + dateList[2]
        return redirect(red)
    return render(request, "export.html", locals())



def export_user_xls(request, mDate):
    year = mDate[0:4]
    month = mDate[4:6]
    days = mDate[6:8]
    mSheetname = year + '-' + month + '-' + days + '訂購單'
    mFilename = 'attachment; filename='+year+'-'+month+'-'+days+'.xls'
    int(year)
    int(month)
    int(days)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = mFilename

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(mSheetname)

    row_num = 0



    columns = ['訂購者','取貨地點','聯絡電話','取貨日期',
             '鮮奶吐司', '鮮奶吐司-切片', '鮮奶吐司-厚度', '葡萄乾吐司', '葡萄乾吐司-切片', '葡萄乾吐司-厚度',
             '蔓越莓吐司', '蔓越莓吐司-切片', '蔓越莓吐司-厚度', '核桃吐司', '核桃吐司-切片', '核桃吐司-厚度',
             '酵母鬆餅', '酵母鬆餅-切片']
    for col_num in range(len(columns)):
        col = ws.col(col_num)
        col.width = 256 * 25
        font_style = xlwt.easyxf('font:height 350; align: horiz center')
        myrow = ws.row(0)
        myrow.set_style(font_style)
        ws.write(row_num, col_num, columns[col_num], font_style)


    rows = order.objects.filter(cDate__year=year,cDate__month=month, cDate__day=days).values_list('cName','cSpot','cPhone','cDate',
             'c1T100', 'c1T100_slice', 'c1T100_thickless', 'c1T120', 'c1T120_slice', 'c1T120_thickless',
             'c1T130', 'c1T130_slice', 'c1T130_thickless', 'c1T140', 'c1T140_slice', 'c1T140_thickless',
             'c2M50', 'c2M50_slice')

    for row in rows:
        row_num += 1
        font_style = xlwt.easyxf('font:height 300; align: horiz center')
        myrow = ws.row(row_num)
        myrow.set_style(font_style)
        for col_num in range(len(row)):
            if col_num == 3:
                time = row[col_num].strftime('%Y-%m-%d')
                ws.write(row_num, col_num, time, font_style)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response


def check(request):
    mDate= request.GET.get('Date', None)
    dateList = [x for x in mDate.split("/")]
    year = int(dateList[0].strip())
    month = int(dateList[1].strip())
    days = int(dateList[2].strip())
    total = 0
    orderlist = None
    orderlist = order.objects.filter(cDate__year=year,cDate__month=month, cDate__day=days)
    available = True
    canBuy = 0


    for myorder in orderlist:
        total += myorder.c1T100 + myorder.c1T120 + myorder.c1T130 + myorder.c1T140


    if total >= 11:
        available = False
    else:
        available = True
        canBuy = 11 - total

    data = {
        'canBuy' : canBuy,
        'available': available
    }
    return JsonResponse(data)

def myorder(request):
    if request.method == "POST":
        orderform = OrderForm(request.POST)
        if orderform.is_valid():
            cName = orderform.cleaned_data['cName']
            cSpot = orderform.cleaned_data['cSpot']
            cPhone = orderform.cleaned_data['cPhone']
            cDate = orderform.cleaned_data['cDate']

            c1T100 = orderform.cleaned_data['c1T100']
            c1T100_slice = orderform.cleaned_data['c1T100_slice']
            c1T100_thickless = orderform.cleaned_data['c1T100_thickless']

            c1T120 = orderform.cleaned_data['c1T120']
            c1T120_slice =orderform.cleaned_data['c1T120_slice']
            c1T120_thickless = orderform.cleaned_data['c1T120_thickless']

            c1T130 = orderform.cleaned_data['c1T130']
            c1T130_slice =orderform.cleaned_data['c1T130_slice']
            c1T130_thickless = orderform.cleaned_data['c1T130_thickless']

            c1T140 = orderform.cleaned_data['c1T140']
            c1T140_slice =orderform.cleaned_data['c1T140_slice']
            c1T140_thickless = orderform.cleaned_data['c1T140_thickless']

            c2M50 = orderform.cleaned_data['c2M50']
            c2M50_slice =orderform.cleaned_data['c2M50_slice']

            unit = order.objects.create(cName=cName, cSpot=cSpot, cPhone=cPhone, cDate=cDate,
                                        c1T100=c1T100, c1T100_slice=c1T100_slice, c1T100_thickless=c1T100_thickless,
                                        c1T120=c1T120, c1T120_slice=c1T120_slice, c1T120_thickless=c1T120_thickless,
                                        c1T130=c1T130, c1T130_slice=c1T130_slice, c1T130_thickless=c1T130_thickless,
                                        c1T140=c1T140, c1T140_slice=c1T140_slice, c1T140_thickless=c1T140_thickless,
                                        c2M50=c2M50, c2M50_slice=c2M50_slice)
            unit.save()
            message = '訂購完成!'
            return redirect('/success')
        else:
            message = '驗證碼錯誤!'
            orderform = OrderForm()
    else:
        message = '姓名、連絡電話、取貨日期必須輸入!'
        orderform = OrderForm()
    return render(request, "order.html", locals())


def success(request):
    return render(request, "success.html", locals())
