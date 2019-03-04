#coding=utf-8
from util.operation_excel import operation_excel
from method.runmethod import runmethod
from data.dataconfig import row_id
from util.op_json import op_json
class main_run:
    def __init__(self):
        #定义引用类实例
        self.excel_data = operation_excel()
        self.methods=runmethod()
        self.dataconfigs = row_id()
        self.op_json1 = op_json()
        self.op_json2= op_json(r"D:\学习资料\接口自动化\接口自动化-视频\interfaceauto\interface_autoframe\dataconfig\headers.json")
    def main_run(self,excel_path=None):
        #获取表格列头对应列数
        r_me=self.dataconfigs.get_method()
        r_he=self.dataconfigs.get_header()
        r_da=self.dataconfigs.get_requestdata()
        r_url=self.dataconfigs.get_url()
        #获取表格行数
        col_len=self.excel_data.get_colcount()
        #循环执行表格行数据
        for i in range(1,col_len):
            #请求地址、方法、请求头
            url=self.excel_data.get_cellvalus(i,r_url)
            methodes=self.excel_data.get_cellvalus(i,r_me)
            headerss=self.excel_data.get_cellvalus(i,r_he)
            headers_data=self.op_json2.get_value(headerss)
            #获取请求数据别名，并获取对应的json格式请求数据
            data=self.excel_data.get_cellvalus(i,r_da)
            data_json=self.op_json1.get_value(data)
            res=self.methods.method_main(methodes,url,data_json,headers_data)
            print(res)


if __name__ == '__main__':
    test_run=main_run()
    test_run.main_run()


