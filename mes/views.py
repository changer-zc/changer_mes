from django.shortcuts import render,redirect
from mes import models
from urllib import request
from django.shortcuts import render
#连接mysql的类
import pymysql
#引入项目的settings文件
from django.conf import settings
# Create your views here.
def add1(request):
    if request.method == 'GET':
        return render(request,'add1.html')
    else:
        test1 = request.POST.get('record_no')
        test2 = request.POST.get('sn')
        test3 = request.POST.get('board_sn')
        test4 = request.POST.get('mac1')
        test5 = request.POST.get('mac2')
        if models.test.objects.filter(test2=test2):
            print("已有该数据，不要重复添加")
            test = models.test.objects.values()[:10]
            test = list(test)
            print(test)
            error_str = "已有该数据，不要重复添加"
            return render(request,'add1.html',{"test":test,"error_str":error_str})
        else:
            test_save = models.test(test1=test1,test2=test2,test3=test3,test4=test4,test5=test5)
            test_save.save()
            print("11111")
            test = models.test.objects.values()[:10]
            test = list(test)
            print(test)
            return render(request,'add1.html',{"test":test})









#-----这个是/主界面页面引用函数
def index(request):
    #     ""返回首页的页面"""
    #获取学生信息
    try:
        students = get_student()
        #正常展示在页面
        return render(request, 'index.html', {'students': students})
    except Exception as e:
        #如果连接出错，在错误页面展示信息
        error_info = "连接数据库出现异常，具体原因："+ str(e)
        return render(request,'error.html',{'msg':error_info})

#-----------------------这个是mysql数据库连接函数-------------------------------
def get_student():
    """获取数据库信息"""
    db_info = settings.DATABASES['mysql']
    #实例化一个连接
    mysql_conn = pymysql.connect(db_info['HOST'],db_info['USER'],db_info['PASSWORD'],db_info['DB'])
    #获取操作指针
    cursor = mysql_conn.cursor()
    #准备sql语句
    sql = "select * from user;"
    #执行
    try:
        #执行SQL语句
        cursor.execute(sql)
        #获取表所有信息
        results = cursor.fetchall()
        #返回
        return  results

    except Exception as e :
        raise e
        return ("错误的")






















#--------------------------------------分割线
#-----------------这个是/test02页面引用函数
def test(request1):#这个是做异常处理，调用下面这个函数，然后判断正常就返回，注意函数的参数，纠结了很久，然后再在urls。py里面去更改url路径和对应使用哪个函数，这个是最简单的连接sqlserver的,其他的我觉得太复杂，不学了，学一样连接方式就行了
    # try:

    results = today_info()
    count_list = production()
    # real_count = real_count_list()
    return render(request1,'test02.html',{'sql_server_results':results,'count_list':count_list,})

# except Exception as e:
#     error_info = "连接数据库出现异常，具体原因：" + str(e)

#     return render(request1, 'error.html', {'msg': error_info})










#-------------------------以下是sqlserver数据库连接的函数----------------------------------
def sql_server_get():#这个是连接数据库查询，然后然后结果，是一个查询函数
    import pymssql
    import re
    sql_server_conn = pymssql.connect(host='10.130.1.253', user='barcode', password='barcodefornexcom',
                                      database='MIS')
    sql_server_cursor = sql_server_conn.cursor()
    sql_server_cursor.execute('select iom01 from invoice_master; ')
    sql_server_resluts = sql_server_cursor.fetchall()  # 取出来的单个数据是元组，要进行格式化成字符串，然后去掉所有符号
    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n。！，]+'  # 这个是多有需要替换的符号
    results1 = re.sub(r, '', str(sql_server_resluts[0]))  # 格式化成字符串后再把所有符号替换成''
    results2 = re.sub(r, '', str(sql_server_resluts[1]))
    results3 = re.sub(r, '', str(sql_server_resluts[2]))
    results4 = re.sub(r, '', str(sql_server_resluts[3]))
    sql_server_all = [results1, results2, results3, results4]
    return sql_server_all


def today_info():#查询当日在做的工单号，并且相关数据192.168.220.128

    import pymssql
    # 连接sqlserver数据库
    sql_server_conn = pymssql.connect(host='10.130.1.253', user='barcode', password='barcodefornexcom',
                                      database='MIS')
    # 查询出当天做的工单号
    sql_server_cursor = sql_server_conn.cursor()
    sql_server_cursor.execute(
        'select  form_id,form_no  from maf_master order by create_date desc ; ')  # 要看当日生产的哪个工单，只能利用这个时间来对比，今天在做的序号是哪个工单的，再看这个工单的数据
    aaa = sql_server_cursor.fetchone()
    # 保存用做查询的工单号
    form_no = aaa[1].strip()
    # 设置各工站的变量
    operate1 = "Q0015"
    operate2 = "Q0013"
    operate3 = "Q0016"
    operate4 = "Q0022"
    operate5 = "Q0020"
    # 完整的工单号码
    today_info = (aaa[0].strip() + '-' + aaa[1].strip())

    # 进行第一个工站的生产量查询
    sql_server_cursor1 = sql_server_conn.cursor()
    sql_server_cursor1.execute(
        "select count(*)number from maf_master where form_no='%s' and operator='%s' ;" % (form_no, operate1))
    bbb = str(list(sql_server_cursor1.fetchone())[0])
    print("正在生产工单：" + today_info)
    print("组装站：" + bbb)

    # 进行第二个工站的生产量查询
    sql_server_cursor2 = sql_server_conn.cursor()
    sql_server_cursor2.execute(
        "select count(*)number from maf_master where form_no='%s' and operator='%s';" % (form_no, operate2))
    ccc = str(list(sql_server_cursor2.fetchone())[0])
    print("基测站：" + ccc)

    # 进行第三个工站的生产量查询
    sql_server_cursor3 = sql_server_conn.cursor()
    sql_server_cursor3.execute(
        "select count(*)number from maf_master where form_no='%s' and operator='%s';" % (form_no, operate3))
    ddd = str(list(sql_server_cursor3.fetchone())[0])
    print("烧机站：" + ddd)

    # 进行第四个工站的生产量查询
    sql_server_cursor4 = sql_server_conn.cursor()
    sql_server_cursor4.execute(
        "select count(*)number from maf_master where form_no='%s' and operator='%s';" % (form_no, operate4))
    eee = str(list(sql_server_cursor4.fetchone())[0])
    print("功测站：" + eee)

    # 进行第五个工站的生产量查询
    sql_server_cursor5 = sql_server_conn.cursor()
    sql_server_cursor5.execute(
        "select count(*)number from maf_master where form_no='%s' and operator='%s';" % (form_no, operate5))
    fff = str(list(sql_server_cursor5.fetchone())[0])
    print("包装站：" + fff)

    all_info = [today_info, bbb, ccc, ddd, eee, fff]
    sql_server_conn.close()

    # 查询另外一个数据库中今天这个工单的计划生产量
    sql_server_conn_NEXCOM = pymssql.connect(host='10.130.1.253', user='barcode', password='barcodefornexcom',
                                             database='NEXCOM')
    sql_server_conn__NEXCOM_cursor = sql_server_conn_NEXCOM.cursor()
    sql_server_conn__NEXCOM_cursor.execute("select TA015 from MOCTA where TA002='%s' ;" % (form_no))
    today_info_allcount = int(list(sql_server_conn__NEXCOM_cursor.fetchone())[0])


    #完成率=包装站完成数量/总数量
    completion_rate = int(fff)/today_info_allcount
    #要把小数点换算成百分比
    completion_rate = "%.2f%%"%(completion_rate*100)


    #未完成量=总量-最后一个工站量
    today_info_weiwancheng = int(today_info_allcount)-int(fff)


    all_info.append(today_info_allcount)
    all_info.append(completion_rate)
    all_info.append(today_info_weiwancheng)
    return all_info




















#查询当月工单生产量，机型，数量，不良率
def production():
    import pymssql
    import datetime
    # 连接sqlserver数据库
    sql_server_conn = pymssql.connect(host='10.130.1.253', user='barcode', password='barcodefornexcom',
                                      database='MIS')
    now = datetime.datetime.today()
    now_year = str(now.year)
    now_mon = str(now.month)
    sql_server_conn_production = sql_server_conn.cursor()
    sql = "select form_no from maf_master where operator='q0020' and DATEPART(year,create_date)='%s' and DATEPART(m,create_date)='%s' group by form_no" % (now_year,now_mon)
    sql_server_conn_production.execute(sql)
    record_count = sql_server_conn_production.fetchall()#查询出的工单数据
    list_item_count = len(record_count)#查询出的工单个数
    new_list = []#空列表
    for i in range(0,list_item_count):
        new_list.append(record_count[i][0])#因为查询出来的是元组，把元素循环遍历加入到这个空的List中

    #以上是查询当月生产了哪些工单，并且元组结构的数据集改成列表模式



    #循环查询列表工单的预计生产数量
    count_list = []#定义一个空列表
    i = 0
    real_count = real_count_list()
    print(real_count)
    print(real_count[0])
    while i < list_item_count:#当i小于当月生产工单数量时执行
        sql_server_conn_production_count = sql_server_conn.cursor()
        sql = "use NEXCOM;select TA002,TA006,TA015,TA034 from MOCTA where TA002='%s'" % (new_list[i])#依次执行查询工单预计生产量
        sql_server_conn_production_count.execute(sql)
        # a = 'sql_server_production_count'+str(i)
        a = sql_server_conn_production_count.fetchall()#查询出的结果是一个列表里面包含元组
        # a = a[0] + real_count[i]
        b = a[0] + real_count[i]#元组可以这样添加元素
        print(b)
        count_list.append(b)#把查询出一个工单的元组数据添加到列表中
        i = i + 1#增加1继续循环，直到当月生产工单列表中的总个数
    print(count_list)
    return count_list
    # return render(request2,"test02.html",{"count_list":count_list})








#查询这个月每个工单实际生产的数量
def real_count_list():
    import pymssql
    import datetime
    # 连接sqlserver数据库
    sql_server_conn = pymssql.connect(host='10.130.1.253', user='barcode', password='barcodefornexcom',
                                      database='MIS')
    now = datetime.datetime.today()
    now_year = str(now.year)
    now_mon = str(now.month)
    sql_server_conn_production = sql_server_conn.cursor()
    sql = "select form_no from maf_master where operator='q0020' and DATEPART(year,create_date)='%s' and DATEPART(m,create_date)='%s' group by form_no" % (now_year,now_mon)
    sql_server_conn_production.execute(sql)
    record_count = sql_server_conn_production.fetchall()#查询出的工单数据
    list_item_count = len(record_count)#查询出的工单个数
    new_list = []#空列表
    for i in range(0,list_item_count):
        new_list.append(record_count[i][0])#因为查询出来的是元组，把元素循环遍历加入到这个空的List中

    #以上是查询当月生产了哪些工单，并且元组结构的数据集改成列表模式
    real_count_list = []
    x = 0
    while x < list_item_count:
        sql_server_conn_real_count = sql_server_conn.cursor()
        sql1 = "select count(sn) from maf_master where form_no='%s' and operator='Q0020'" % (new_list[x])
        sql_server_conn_real_count.execute(sql1)
        a1 = sql_server_conn_real_count.fetchall()
        real_count_list.append(a1[0])
        x = x + 1
    return real_count_list















#查询12个月每月生产的数量
def every_month_count():
    import pymssql
    import datetime
    # 连接sqlserver数据库
    sql_server_conn = pymssql.connect(host='10.130.1.253', user='barcode', password='barcodefornexcom',
                                      database='MIS')
    now = datetime.datetime.today()
    now_year = str(now.year)
    now_mon = str(now.month)
    sql_server_conn_production = sql_server_conn.cursor()
    sql = "select form_no from maf_master where operator='q0020' and DATEPART(year,create_date)='%s' and DATEPART(m,create_date)='%s' group by form_no" % (now_year,now_mon)
    sql_server_conn_production.execute(sql)
    record_count = sql_server_conn_production.fetchall()#查询出的工单数据
    list_item_count = len(record_count)#查询出的工单个数
    print(list_item_count)
    new_list = []#空列表
    for i in range(0,list_item_count):
        new_list.append(record_count[i][0])#因为查询出来的是元组，把元素循环遍历加入到这个空的List中
    print(new_list)
    #以上是查询当月生产了哪些工单，并且元组结构的数据集改成列表模式



    #循环查询列表工单的预计生产数量
    count_list = []#定义一个空列表
    i = 0
    while i < list_item_count:#当i小于当月生产工单数量时执行
        sql_server_conn_production_count = sql_server_conn.cursor()
        sql = "use NEXCOM;select TA002,TA006,TA015,TA034 from MOCTA where TA002='%s'" % (new_list[i])#依次执行查询工单预计生产量
        sql_server_conn_production_count.execute(sql)
        # a = 'sql_server_production_count'+str(i)
        a = sql_server_conn_production_count.fetchall()#查询出的结果是一个列表里面包含元组
        count_list.append(a[0])#把查询出一个工单的元组数据添加到列表中
        i = i + 1#增加1继续循环，直到当月生产工单列表中的总个数


    #再循环查出每个工单当月实际生产量
    # real_count_list = []
    # x = 0
    # while x < list_item_count:
    #     sql_server_conn_real_count = sql_server_conn.cursor()
    #     sql1 = "select count(sn) from MIS where form_no='%s' and operator='Q0020'" % (new_list[x])
    #     sql_server_conn_real_count.execute(sql1)
    #     a1 = sql_server_conn_real_count.fetchall()
    #     count_list.append(a1[0])
    #     x = x + 1

    return count_list




