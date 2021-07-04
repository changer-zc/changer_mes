from import_export import resources
from mes.models import out_record,in_record,ware_house

class out_record_Resourse(resources.ModelResource):
    def get_export_headers(self):
        return ['料号','名称','数量','客户','出货地址','出货时间']

    class Meta:
        module = out_record
        report_skipped = False

class in_record_Resourse(resources.ModelResource):
    class Meta:
        __module__ = in_record



class ware_house_Resourse(resources.ModelResource):
    def get_export_headers(self):
        return ['料号','名称','数量','位置','供应商','盘点时间']
    # def get_fields(self, **kwargs):
    #     return ('item_no','item_name','numbers','location','supplier','inventory_time',)
    # def get_export_order(self):
    #
    #     return ('item_no','item_name','numbers','location','supplier','inventory_time',)
    def get_export_fields(self):
        return ('item_no','item_name','numbers','location','supplier','inventory_time',)
    class Meta:
        __module__ = ware_house







