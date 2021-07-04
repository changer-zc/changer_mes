from django.contrib import admin
from django.contrib import admin,messages
from django.db import transaction
from django.urls import reverse
from .models import *
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin
from import_export import resources
import simpleui
from mes import views
from mes import resourse
from .models import ware_house
from django.core.exceptions import ImproperlyConfigured
#---------django信号机制----------
from django.db.models.signals import post_save
from django.dispatch import receiver
#---------django信号机制----------
# Register your models here.







#---------------------------------------维修--------------------------------------
#-------------维修记录----------------
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


#--------------维修治具-------------------
class tools_record_Admin(admin.ModelAdmin):
    #显示的字段
    list_display = ('tool_name','tool_num','descript')
    #点击保存并继续编辑这个按钮给取消掉
    save_as_continue = False
    #列表页搜索字段
    search_fields = ('tool_name',)
    #这个就牛逼了，下面这个函数，会让模型表可以正常添加，但是不能编制，添加后只能查看
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields+('tool_name',)
        return self.readonly_fields
admin.site.register(tools_record,tools_record_Admin)




#-----------------维修报废-------------------
class repair_scrap_Admin(admin.ModelAdmin):
    #显示的字段
    list_display = ('item_name','descript','scrap_time')
    #点击保存并继续编辑这个按钮给取消掉
    save_as_continue = False
    #列表页搜索字段
    search_fields = ('item_name',)
    #这个就牛逼了，下面这个函数，会让模型表可以正常添加，但是不能编制，添加后只能查看
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields+('item_name','descript','scrap_time')
        return self.readonly_fields
admin.site.register(repair_scrap,repair_scrap_Admin)

















#-------------------------------质检---------------------------------------
#------------------------------来料质检------------------------------------
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
    #这个就牛逼了，下面这个函数，会让模型表可以正常添加，但是不能编写，添加后只能查看
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields+('material_name','material_sn','arrive_time','appearance','arrive_num','bad_num','supplier')
        return self.readonly_fields

admin.site.register(IQC,IQC_Admin)


#生产质检
class production_IQC_Admin(admin.ModelAdmin):
    #显示的字段
    list_display = ('production_name','work_order','bad_num','describe','happen_time')
    #每页展示的条数
    list_per_page = 30
    #点击保存并继续编辑这个按钮给取消掉
    save_as_continue = False
    #列表页搜索字段
    search_fields = ('production_name','work_order')
    #列表页上时间搜索
    date_hierarchy = 'happen_time'
    #这个就牛逼了，下面这个函数，会让模型表可以正常添加，但是不能编写，添加后只能查看
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields+('production_name','work_order','bad_num','describe','happen_time')
        return  self.readonly_fields
admin.site.register(production_IQC,production_IQC_Admin)





#出货质检
class out_IQC_Admin(admin.ModelAdmin):
    #显示的字段
    list_display = ('production_name','work_order','all_num','bad_num','describe','happen_time')
    #每页展示的条数
    list_per_page = 30
    #点击保存并继续编辑这个按钮给取消掉
    save_as_continue = False
    #列表页搜索字段
    search_fields = ('production_name','work_order')
    #列表页上时间搜索
    date_hierarchy = 'happen_time'
    #这个就牛逼了，下面这个函数，会让模型表可以正常添加，但是不能编写，添加后只能查看
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields+('production_name','work_order','all_num','bad_num','describe','happen_time')
        return  self.readonly_fields
admin.site.register(out_IQC,out_IQC_Admin)
#---------------------------------------------------------------------------------------------------




















#=-------------------------------------------库存------------------------------------------



class ware_house_Admin(ImportExportActionModelAdmin):
    #显示的字段
    list_display = ('item_no','item_name','numbers','location','supplier','inventory_time',)
    # resource_class = ware_house_resource
class ware_house_resource(resources.ModelResource):
    class Meta:
        __module__ = ware_house
        fields = ('item_no','item_name','numbers','location','supplier','inventory_time',)



admin.site.register(ware_house,ware_house_Admin)



#出货记录
class out_record_Admin(ImportExportActionModelAdmin,admin.ModelAdmin):
    #显示的字段
    list_display = ('item_no','item_name','numbers','customer','out_address','out_time',)
    #每页展示的条数
    list_per_page = 30
    #点击保存并继续编辑这个按钮给取消掉
    save_as_continue = False
    #列表页搜索字段
    search_fields = ('item_no','item_name',)
    #导出功能
    resource_class = resourse.out_record_Resourse

    #列表页上时间搜索
    date_hierarchy = ('out_time')
    #这个就牛逼了，下面这个函数，会让模型表可以正常添加，但是不能编写，添加后只能查看
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields+('item_no','item_name','numbers','customer','out_address','out_time',)
        return  self.readonly_fields

#使用dajngo的信号机制，在点击保存后，执行此函数，sender是发送信号的模型,instance本身
    @receiver(post_save,sender=out_record)
    def update_ware_house(sender,instance,**kwargs):
        a = ware_house.objects.filter(item_name = instance.item_name)[0]
        b = str(int(a.numbers)-int(instance.numbers))
        a.numbers = b
        a.save()
    print("更改成功")

admin.site.register(out_record,out_record_Admin)







#入库记录
class in_record_Admin(ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ('item_no','item_name','numbers','supplier','in_time',)
    #每页展示的条数
    list_per_page = 30
    #点击保存并继续编辑这个按钮给取消掉
    save_as_continue = False
    #导入导出功能
    resource_class = resourse.in_record_Resourse
    #列表页搜索字段
    search_fields = ('item_no','item_name',)
    #列表页上时间搜索
    date_hierarchy = ('in_time')

    #这个就牛逼了，下面这个函数，会让模型表可以正常添加，但是不能编写，添加后只能查看
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields+('item_no','item_name','numbers','supplier','in_time',)
        return  self.readonly_fields

    @receiver(post_save,sender=in_record)
    def update_ware_house(sender,instance,**kwargs):
        a = ware_house.objects.filter(item_name = instance.item_name)[0]
        b = str(int(a.numbers)+int(instance.numbers))
        a.numbers = b
        a.save()



admin.site.register(in_record,in_record_Admin)
#--------------------------------------------------------------------------------------------------








#-----------------------------------------生产--------------------------------------------
#版本维护
class version_manager_Admin(admin.ModelAdmin):
    list_display = ('item_name','version','descript','update_time')
    #点击保存并继续编辑这个按钮给取消掉
    save_as_continue = False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields+('item_name',)
        return  self.readonly_fields

admin.site.register(version_manager,version_manager_Admin)
















#--------------------------------------------测试测试测试测试测试测试测试 -----------------------------------------------

def test_action(modeladmin,request,queryset):
    #自动修改本表模型字段
    queryset.update(test5 = "进行中")
    #自动修改其他表模型字段
    a = queryset[0].test1
    b = ware_house.objects.filter(item_name = a)
    b.update(supplier = "已完结")
test_action.short_description = "测试生成订单"
@admin.register(test)
class test_Admin(admin.ModelAdmin):
    list_display = ('test1','test2','test3','test4','test5')
    actions = [test_action]

