from django.shortcuts import render,redirect
from mes import models
from urllib import request
from django.shortcuts import render
#连接mysql的类
import pymysql
#引入项目的settings文件
from django.conf import settings


def test2(request1):
    #数据渲染auto_sop网页

    aaa = input_web()
    #判断远程执行cmd命令
    bbb = execute_open()
    return render(request1,'auto_sop.html',{'input_web':aaa,'execute_open':bbb,})


def input_web():
    import pymssql
    # 连接sqlserver数据库
    sql_server_conn = pymssql.connect(host='192.168.118.128', user='barcode', password='barcodefornexcom',
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
    record_number = aaa[1].strip()
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



    #查询该工单使用的料号
    sql_server_cursor6 = sql_server_conn.cursor()
    sql_server_cursor6.execute("select item_no from assyset where ta_no='%s'  " % (today_info,))
    ggg = str(list(sql_server_cursor6.fetchone())[0])
    print("工单料号：" + ggg)

    #查询该工单是哪个机种，该机种是哪个版本号
    # sql_server_cursor6 = sql_server_conn.cursor()
    # sql_server_cursor6.execute("USE NEXCOM; select TA034 from MOCTA where TA002='%s'" % (record_number))
    # ggg = str(list(sql_server_cursor6.fetchone())[0])
    # print("ggg:"+ggg)
    # hhh = (models.version_manager.objects.filter(item_name=ggg).values())[0].get('version')
    # print(hhh)



    all_info = [today_info, bbb, ccc, ddd, eee, fff]
    sql_server_conn.close()

    # 查询另外一个数据库中今天这个工单的计划生产量
    sql_server_conn_NEXCOM = pymssql.connect(host='192.168.118.128', user='barcode', password='barcodefornexcom',
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
    all_info.append(ggg)
    # all_info.append(hhh)
    print(all_info)
    return all_info



def execute_open():
    import winrm
    import pymssql
    #查看最新一条生产数据是在生产哪一个工单
    sql_server_conn = pymssql.connect(host='192.168.118.128', user='barcode', password='barcodefornexcom',
                                      database='MIS')

    sql_server_cursor_OrderNumber = sql_server_conn.cursor()
    sql_server_cursor_OrderNumber.execute("select top 1 form_no from maf_master order by create_date desc ")
    now_order_number = list(sql_server_cursor_OrderNumber.fetchone())[0]
    print(now_order_number)



    #查询这个工单机种名称
    sql_server_conn_NEXCOM = pymssql.connect(host='192.168.118.128', user='barcode', password='barcodefornexcom',
                                      database='NEXCOM')
    sql_server_conn_NEXCOM_ProductionName = sql_server_conn_NEXCOM.cursor()
    sql_server_conn_NEXCOM_ProductionName.execute("select TA034 from MOCTA where TA002 = '%s';" % (now_order_number))
    now_production_name = list(sql_server_conn_NEXCOM_ProductionName.fetchone())[0]
    print(now_production_name)


    #展示图片的路径
    aaaaaa = now_production_name+".jpg"


    print(aaaaaa)
    a = list()
    a.append(now_order_number)
    a.append(now_production_name)
    a.append(aaaaaa)
    print(a)


    #远程执行CMD命令
    import os
    os.system('start "" "F:\自己私人\自己开发的软件\c.bat" ')


    return a








