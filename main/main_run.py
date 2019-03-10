#coding=utf-8
from util.operation_excel import operation_excel
from method.runmethod import runmethod
from data.dataconfig import row_id
from data.get_data import GETDATA
from util.op_json import op_json
from util.cmp_str import com_str
import json
class main_run:
    def __init__(self):
        #定义引用类实例
        self.methods=runmethod()
        self.dataconfigs = row_id()
        self.getdata=GETDATA()
        self.cmpre=com_str()
        self.op_json1 = op_json()
        self.op_json2= op_json(r"D:\学习资料\接口自动化\接口自动化-视频\interfaceauto\interface_autoframe\dataconfig\headers.json")
    def main_run(self,excel_path=None):
        #获取表格列头对应列数
        excel_data = operation_excel(excel_path)
        r_me=self.dataconfigs.get_method()
        r_he=self.dataconfigs.get_header()
        r_da=self.dataconfigs.get_requestdata()
        r_url=self.dataconfigs.get_url()
        r_isrun=self.dataconfigs.get_isrun()
        #获取表格行数
        col_len=excel_data.get_colcount()
        res=None
        right_count=0
        wrong_count=0
        #循环执行表格行数据
        for i in range(1,col_len):
            #请求地址、方法、请求头
            url=self.getdata.get_url_data(i)
            methodes=self.getdata.get_method_data(i)
            filepath_header = r"../dataconfig/headers.json"
            headerss=self.getdata.get_header_data(i,filepath_header)
            #print(headerss)
            is_run=self.getdata.get_isrun_data(i)
            #print(is_run)
            #获取请求数据别名，并获取对应的json格式请求数据
            data=self.getdata.get_request_data(i)
            expect_result=self.getdata.get_expect_data(i)
            print(type(expect_result))
            #print(type(excel_data))
            if is_run==True:
                res=self.methods.method_main(methodes,url,data,headerss,)
                self.getdata.write_data(i,json.dumps(res,ensure_ascii=False))
                print(type(res))
                if self.cmpre.com_result(expect_result,res)==True:
                    right_count=right_count+1
                else:
                    wrong_count=wrong_count+1
        print("正确：%d,错误：%d," % (right_count,wrong_count))



if __name__ == '__main__':
    test_run=main_run()
    test_run.main_run()


