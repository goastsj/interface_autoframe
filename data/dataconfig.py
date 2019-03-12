#coding utf-8
from util.operation_excel import operation_excel
class row_id:
    #d定义列头顺序，获取列头位置
    id=0
    name=1
    url=2
    is_run=3
    method=4
    headers=5
    case_depend=6
    depend_responce=7
    data_depend=8
    request_data=9
    expect_result=10
    result=11
    #def __init__(self):
        #self.excel_data=operation_excel()
    #获取用例id
    def get_id(self):
        #id_value=self.excel_data.get_cellvalus(rows,row_id.id)
        return row_id.id

    #获取用例名称
    def get_name(self):

        return row_id.name

    #获取请求地址
    def get_url(self):
        return row_id.url

    #获取是否运行
    def get_isrun(self):
        return row_id.is_run

    #获取请求方法
    def get_method(self):
        return row_id.method

    #获取header
    def get_header(self):
        return row_id.headers

    #获取用例依赖
    def get_casedepend(self):
        return row_id.case_depend

    #获取依赖返回内容
    def get_rependrespond(self):
        return row_id.depend_responce

    #获取数据依赖字段
    def get_datarespond(self):
        return row_id.data_depend
    #获取请求数据
    def get_request(self):
        return row_id.request_data

    #获取期望结果字段
    def get_expectrespond(self):
        return row_id.expect_result

    #获取实际结果
    def get_result(self):
        return row_id.result
    #获取请求数据
    def get_requestdata(self):
        return row_id.request_data

if __name__ == '__main__':
    getrows=row_id()
    a=getrows.get_id(2)
    print(a)




