# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.exceptions import ImproperlyConfigured


# -------------------------------------------维修-----------------------------------------------------------
#------维修记录------
class Repair(models.Model):
    item_no = models.CharField(max_length=255, blank=True, null=True,verbose_name='料号')
    product_name = models.CharField(max_length=255, blank=True, null=True,verbose_name='品名')
    part_or_complete = models.IntegerField(blank=True, null=True,verbose_name='部件/征集',choices=((1,'部件'),(0,'整机')),default='整机')
    collect_money = models.IntegerField(blank=True, null=True,verbose_name='是否要收款',choices=((1,'是'),(0,'否')),default='是')
    collect_money_num = models.CharField(max_length=255,blank=True,null=True,verbose_name='需要收款价格')
    sn = models.CharField(max_length=255, blank=True, null=True,verbose_name='整机SN')
    board_sn = models.CharField(max_length=255, blank=True, null=True,verbose_name='主板SN')
    statu = models.IntegerField(blank=True, null=True,verbose_name='维修状态',choices=((2,'已接收'),(1,'维修中'),(0,'已修复')),default='已接收')
    be_overdue = models.IntegerField(blank=True, null=True,verbose_name='是否过保',choices=((1,'已过保'),(0,'未过保')),default='未过保')
    receive_time = models.DateTimeField(blank=True, null=True,verbose_name='接收时间')
    repair_time = models.DateTimeField(blank=True, null=True,verbose_name='修复时间')
    out_time = models.DateTimeField(blank=True,null=True,verbose_name='交出时间')
    class Meta:
        managed = True
        db_table = 'repair'
        verbose_name = '维修'



#---------维修治具-------------
class tools_record(models.Model):
    tool_name = models.CharField(max_length=255, blank=True, null=True,verbose_name='工具名')
    tool_num = models.CharField(max_length=255, blank=True, null=True,verbose_name='数量')
    descript = models.CharField(max_length=255, blank=True, null=True,verbose_name='备注')
    class Meta:
        managed = True
        db_table = 'tools_record'
        verbose_name = '维修治具'



#---------------维修报废---------------
class repair_scrap(models.Model):
    item_name = models.CharField(max_length=255, blank=True, null=True,verbose_name='报废料件名称')
    descript = models.CharField(max_length=255, blank=True, null=True,verbose_name='报废原因描述')
    scrap_time = models.DateTimeField(blank=True, null=True,verbose_name='报废时间')
    class Meta:
        managed = True
        db_table = 'repair_scrap'
        verbose_name = '报废记录'

#--------------------------------------------------------------------------------------------










# --------------------------------------质检--------------------------------------------------------
class IQC(models.Model):
    material_name = models.CharField(max_length=255, blank=True, null=True,verbose_name='物料名称')
    material_sn = models.CharField(max_length=255, blank=True, null=True,verbose_name='料号')
    arrive_time = models.DateTimeField(blank=True, null=True,verbose_name='来料时间')
    appearance = models.IntegerField(blank=True, null=True,verbose_name='外观检测',choices=((1,'合格'),(0,'不合格')),default='不合格')
    arrive_num = models.CharField(max_length=255, blank=True, null=True,verbose_name='来料数量')
    bad_num = models.CharField(max_length=255, blank=True, null=True,verbose_name='不良数量')
    supplier = models.CharField(max_length=255, blank=True, null=True,verbose_name='供应商')


    class Meta:
        managed = True
        db_table = 'IQC'
        verbose_name = '质检'

#生产质检记录
#出现生产线问题导致重工或者停线的记录下来
class production_IQC(models.Model):
    production_name = models.CharField(max_length=255, blank=True, null=True,verbose_name='名称')
    work_order = models.CharField(max_length=255, blank=True, null=True,verbose_name='工单号')
    bad_num = models.CharField(max_length=255, blank=True, null=True,verbose_name='不良数量')
    describe = models.CharField(max_length=255, blank=True, null=True,verbose_name='描述')
    happen_time = models.DateTimeField(blank=True, null=True,verbose_name='发生时间')


    class Meta:
        managed = True
        db_table = 'production_IQC'
        verbose_name = '质检'





#出货质检记录
#抽检记录




class out_IQC(models.Model):
    production_name = models.CharField(max_length=255, blank=True, null=True,verbose_name='名称')
    work_order = models.CharField(max_length=255, blank=True, null=True,verbose_name='工单号')
    all_num = models.CharField(max_length=255, blank=True, null=True,verbose_name='抽检总数量')
    bad_num = models.CharField(max_length=255, blank=True, null=True,verbose_name='不良数量')
    describe = models.CharField(max_length=255, blank=True, null=True,verbose_name='问题描述')
    happen_time = models.DateTimeField(blank=True, null=True,verbose_name='抽检时间')


    class Meta:
        managed = True
        db_table = 'out_IQC'
        verbose_name = '出货抽检'
#--------------------------------------------------------------------------------------------










#       ------------------------------     测试-------------------------------------------
class test(models.Model):
    test1 = models.CharField(max_length=255, blank=True, null=True,verbose_name='测试数据1')
    test2 = models.CharField(max_length=255, blank=True, null=True,verbose_name='测试数据2')
    test3 = models.CharField(max_length=255, blank=True, null=True,verbose_name='测试数据3')
    test4 = models.CharField(max_length=255, blank=True, null=True,verbose_name='测试数据4')
    test5 = models.CharField(max_length=255, blank=True, null=True,verbose_name='状态')

    class Meta:
        managed = True
        db_table = 'test'
#--------------------------------------------------------------------------------------------













#   -------------------------------------库房-------------------------------------------------------
#库存
class ware_house(models.Model):
    item_no = models.CharField(max_length=255, blank=True, null=True,verbose_name='料号')
    item_name = models.CharField(max_length=255, blank=True, null=True,verbose_name='名称')
    numbers = models.CharField(max_length=255,blank=True,null=True,verbose_name='数量')
    location = models.CharField(max_length=255, null=True,verbose_name='库位',choices=(('成品仓','成品仓'),('半成品仓','半成品仓'),('电子库房','电子库房')),default='成品仓')
    supplier = models.CharField(max_length=255, blank=True, null=True,verbose_name='厂商')
    inventory_time = models.DateTimeField(blank=True, null=True,verbose_name='盘点时间')


    class Meta:
        managed = True
        db_table = 'ware_house'
        verbose_name = '库存'

#出货记录
class out_record(models.Model):
    item_no = models.CharField(max_length=255, blank=True, null=True,verbose_name='工单号')
    item_name = models.CharField(max_length=255, blank=True, null=True,verbose_name='名称')
    numbers = models.CharField(max_length=255,blank=True,null=True,verbose_name='数量')
    customer = models.CharField(max_length=255, blank=True, null=True,verbose_name='客户')
    out_address = models.CharField(max_length=255, blank=True, null=True,verbose_name='出货地址')
    out_time = models.DateTimeField(blank=True, null=True,verbose_name='出货时间')


    class Meta:
        managed = True
        db_table = 'out_record'
        verbose_name = '出库记录'
#入库记录
class in_record(models.Model):
    item_no = models.CharField(max_length=255, blank=True, null=True,verbose_name='料号')
    item_name = models.CharField(max_length=255, blank=True, null=True,verbose_name='名称')
    numbers = models.CharField(max_length=255,blank=True,null=True,verbose_name='数量')
    supplier = models.CharField(max_length=255, blank=True, null=True,verbose_name='供应商')
    in_time = models.DateTimeField(blank=True, null=True,verbose_name='入库时间')


    class Meta:
        managed = True
        db_table = 'in_record'
        verbose_name = '入库记录'
#盘点
#--------------------------------------------------------------------------------------------








#-----------------------------------生产-------------------------------------------
#----------版本维护-----------------
class version_manager(models.Model):
    item_name = models.CharField(max_length=255, blank=True, null=True,verbose_name='名称')
    version = models.CharField(max_length=255,blank=True,null=True,verbose_name='版本号')
    descript = models.CharField(max_length=255, blank=True, null=True,verbose_name='描述')
    update_time = models.DateTimeField(blank=True, null=True,verbose_name='更新时间')
    class Meta:
        managed = True
        db_table = 'version_manager'
        verbose_name = '版本维护'


