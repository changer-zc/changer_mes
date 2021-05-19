from django.contrib import admin
from django.contrib import admin,messages
from django.db import transaction
from django.urls import reverse
from .models import *
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin
from import_export import resources
import simpleui
from mes import views
# Register your models here.


class Repair_Admin(admin.ModelAdmin):
    #显示的字段
    list_display = ('item_no','product_name','sn','board_sn','statu','be_overdue','receive_time','repair_time','out_time')
    #每页展示的条数
    list_per_page = 30
    #点击保存并继续编辑这个按钮给取消掉
    save_as_continue = False
    #详情页面使用radio显示选项
    radio_fields = {}
    #列表页搜索字段
    search_fields = ('item_no','sn','board_sn','repair_time',)
    #在列表页可以编辑的字段
    list_editable = ('statu','repair_time','out_time')

    #列表页上时间搜索
    date_hierarchy = 'repair_time'
    #这个就牛逼了，下面这个函数，会让模型表可以正常添加，但是不能编制，添加后只能查看
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields+('item_no','product_name','sn','board_sn','statu','be_overdue','receive_time','repair_time')
        return self.readonly_fields

admin.site.register(Repair,Repair_Admin)
#测试一下



class IQC_Admin(admin.ModelAdmin):
    #显示的字段
    list_display = ('material_name','material_sn','arrive_time','appearance','arrive_num','bad_num','supplier')
    #每页展示的条数
    list_per_page = 30
    #点击保存并继续编辑这个按钮给取消掉
    save_as_continue = False
    #详情页面使用radio显示选项
    radio_fields = {}
    #列表页搜索字段
    search_fields = ('material_name','material_sn','supplier')
    #在列表页可以编辑的字段
    list_editable = ('bad_num',)

    #列表页上时间搜索
    date_hierarchy = 'arrive_time'
    #这个就牛逼了，下面这个函数，会让模型表可以正常添加，但是不能编制，添加后只能查看
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields+('material_name','material_sn','arrive_time','appearance','arrive_num','bad_num','supplier')
        return self.readonly_fields

admin.site.register(IQC,IQC_Admin)




class ware_house_Admin(admin.ModelAdmin):
    #显示的字段
    list_display = ('item_no','item_name','numbers','location','supplier','inventory_time',)
admin.site.register(ware_house,ware_house_Admin)