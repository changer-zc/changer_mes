# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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





class test(models.Model):
    test1 = models.CharField(max_length=255, blank=True, null=True,verbose_name='测试数据1')
    test2 = models.CharField(max_length=255, blank=True, null=True,verbose_name='测试数据2')
    test3 = models.CharField(max_length=255, blank=True, null=True,verbose_name='测试数据3')
    test4 = models.CharField(max_length=255, blank=True, null=True,verbose_name='测试数据4')
    test5 = models.CharField(max_length=255, blank=True, null=True,verbose_name='测试数据5')

    class Meta:
        managed = True
        db_table = 'test'



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

