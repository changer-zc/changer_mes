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
    sn = models.CharField(max_length=255, blank=True, null=True,verbose_name='整机SN')
    board_sn = models.CharField(max_length=255, blank=True, null=True,verbose_name='主板SN')
    statu = models.IntegerField(blank=True, null=True,verbose_name='维修状态',choices=((2,'已接收'),(1,'维修中'),(0,'已修复')),default='已接收')
    be_overdue = models.IntegerField(blank=True, null=True,verbose_name='是否过保',choices=((1,'已过保'),(0,'未过保')),default='未过保')
    receive_time = models.DateTimeField(blank=True, null=True,verbose_name='接收时间')
    repair_time = models.DateTimeField(blank=True, null=True,verbose_name='修复时间')

    class Meta:
        managed = True
        db_table = 'repair'
