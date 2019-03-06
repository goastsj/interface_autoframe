#coding='utf-8'
from data.dataconfig import row_id
from util.operation_excel import operation_excel
class GETdata:
    def __init__(self):
        self.row_id=row_id()
        self.op_excel=operation_excel()
    def get_id_data(self,rows):
        id_cols=self.row_id.get_id()
        id_data=self.op_excel.get_cellvalus(rows,id_cols)
        return id_data
    def get_name_data(self,rows):
        name_cols=self.row_id.get_name()
        name_data=self.op_excel.get_cellvalus(rows,name_cols)
        return name_data
    def get_url_data(self,rows):
        url_cols=self.row_id.get_url()
        url_data=self.op_excel.get_cellvalus(rows,url_cols)
        return url_data
    def get_isrun_data(self,rows):
        isrun_cols=self.row_id.get_isrun()
        isrun_data=self.op_excel.get_cellvalus(rows,isrun_cols)
        flag=None
        if isrun_data =='yes':
            flag=true
        else:
            flag=false
        return flag
    def get_method_data(self,rows):
        method_cols=self.row_id.get_method()
        method_data=self.op_excel.get_cellvalus(rows,method_cols)
        return method_data
    def get_header_data(self,rows):
        header_cols=self.row_id.get_header()
        header_data=self.op_excel.get_cellvalus(rows,header_cols)
        if header_data !='':
            header_data=header_data
        else:
            header_data=None
        return header_data
    def get_depend_key(self,rows):
        key_cols=self.row_id.get_casedepend()
        key_data=self.op_excel.get_cellvalus(rows,key_cols)
        if key_data !='':
            key_data=key_data
        else:
            key_data=None
        return key_data
    def get_depend_data(self,rows):
        depend_data_cols=self.row_id.get_datarespond()
        depend_datas=self.op_excel.get_cellvalus(rows,depend_data_cols)
        if depend_datas !='':
            depend_datas=depend_datas
        else:
            depend_datas=None
        return depend_datas
    def get_depend_respond(self,rows):
        depend_respond_cols=self.row_id.get_rependrespond()
        depend_respond_data=self.op_excel.get_cellvalus(rows,depend_respond_cols)
        if depend_respond_data !='':
            depend_respond_data=depend_respond_data
        else:
            depend_respond_data=None
        return depend_respond_data
    def get_request_data(self,rows):
        request_data_cols=self.row_id.get_request()
        request_datas=self.op_excel.get_cellvalus(rows,request_data_cols)
        if request_datas !='':
            request_datas=request_datas
        else:
            request_datas=None
        return request_datas
    #def get_data_json(self,data):
    def get_expect_result(self,rows):
        expect_result_cols=self.row_id.get_expectrespond()
        expect_result_data=self.op_excel.get_cellvalus(rows,expect_result_cols)
        return expect_result_data
    def get_result(self,rows):
        result_cols=self.row_id.get_result()
        result_data=self.op_excel.get_cellvalus(rows,result_cols)
        return result_data
    #获取被依赖的行数据
    def get_depend_returndata(self,keyid):
        nrows=self.op_excel.get_rowcount()
        i=0
        rows_data=None
        for i in range(1,nrows):
            id_data = self.get_id_data(i)
            if id_data==keyid:
                rows_data=self.op_excel.get_rows(i)
                return rows_data

if __name__ == '__main__':
    getdata=GETdata()
    res=getdata.get_depend_returndata('Imooc-11')
    print(res)
    print(type(res))



