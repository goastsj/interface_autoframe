#coding=utf-8
from data.get_data import GETDATA
from method.runmethod import runmethod
from util.operation_excel import operation_excel
from data.dataconfig import row_id
import json
from jsonpath_rw import jsonpath,parse
class GET_Dependdata:
    def __init__(self):
        self.getdata=GETDATA()
        self.runqe=runmethod()
        self.op_excel=operation_excel()
        self.rowid=row_id()
    #获取依赖请求返回数据
    def get_depend_request(self,rowid):
        url=self.getdata.get_url_data(rowid)
        request_data=self.getdata.get_request_data(rowid)
        method=self.getdata.get_method_data(rowid)
        header=self.getdata.get_header_data(rowid)
        #method, url, data = None, headers = None
        res=self.runqe.method_main(method,url,request_data,header)
        return res
    #获取依赖字段的数据
    def get_repend_data(self,case_key,row):
        cols=self.rowid.get_id()
        row_id=self.op_excel.get_row_num(case_key,col=cols)
        res=self.get_depend_request(row_id)
        #print(res)
        repend_dataid=self.getdata.get_case_respond(row)
        #print(repend_dataid)
        #dataid=json.loads(repend_dataid)
        #res=json.loads(res)
        data_path=parse(repend_dataid)
        data=data_path.find(res)
        #print(data)
        datavalues=[]
        datavalues=[datamatch.value for datamatch in data][0]
        return datavalues
if __name__ == '__main__':
    dependdata=GET_Dependdata()
    res=dependdata.get_repend_data("Imooc-11",12)
    print(res)

