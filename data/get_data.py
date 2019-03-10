#coding=utf-8
from data.dataconfig import row_id
from util.operation_excel import operation_excel
from util.op_json import op_json
from util.operation_excel import operation_excel
class GETDATA:
    def __init__(self):
        self.row_id=row_id()
        self.op_excel=operation_excel()
        self.op_jsons=op_json()
    def get_id_data(self,row):
        cols=self.row_id.get_id()
        id_data=self.op_excel.get_cellvalus(row,cols)
        return id_data
    def get_name_data(self,row):
        cols=self.row_id.get_name()
        name_data=self.op_excel.get_cellvalus(row,cols)
        return name_data
    def get_url_data(self,row):
        cols=self.row_id.get_url()
        url_data=self.op_excel.get_cellvalus(row,cols)
        return url_data
    def get_isrun_data(self,row):
        cols=self.row_id.get_isrun()
        flag=None
        isrun_data=self.op_excel.get_cellvalus(row,cols)
        if isrun_data=='yes':
            flag=True
        else:
            flag=False
        return flag
    def get_method_data(self,row):
        cols=self.row_id.get_method()
        method_data=self.op_excel.get_cellvalus(row,cols)
        return method_data
    def get_header_data(self,row,filepath):
        op_jsonhe=op_json(filepath)
        cols=self.row_id.get_header()
        header_data=self.op_excel.get_cellvalus(row,cols)
        if header_data=='':
            header_data=None
        else:
            header_data=op_jsonhe.get_value(header_data)
        return header_data
    def get_case_key(self,row):
        cols=self.row_id.get_casedepend()
        case_key=self.op_excel.get_cellvalus(row,cols)
        if case_key=='':
            case_key=None
        return case_key
    def get_case_respond(self,row):
        cols=self.row_id.get_rependrespond()
        case_respond=self.op_excel.get_cellvalus(row,cols)
        if case_respond=='':
            case_respond=None
        return case_respond
    def get_data_depend(self,row):
        cols=self.row_id.get_datarespond()
        data_depend=self.op_excel.get_cellvalus(row,cols)
        if data_depend=='':
            data_depend=None
        return data_depend
    def get_request_data(self,row):
        cols=self.row_id.get_requestdata()
        quest_id=self.op_excel.get_cellvalus(row,cols)
        quest_data=self.op_jsons.get_value(quest_id)
        if quest_id=='':
            quest_data=None
        return quest_data
    def get_expect_data(self,row):
        cols=self.row_id.get_expectrespond()
        expexct_data=self.op_excel.get_cellvalus(row,cols)
        if expexct_data=='':
            expexct_data=None
        return expexct_data
    def get_result(self,row):
        cols=self.row_id.get_result()
        result=self.op_excel.get_cellvalus(row,cols)
        return result
    def write_data(self,row,values):
        cols=self.row_id.get_result()
        self.op_excel.cell_write(row,cols,values)



