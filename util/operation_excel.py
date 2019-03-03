#coding utf-8
import xlrd
from xlutils.copy import copy


class operation_excel:
    def __init__(self,filename=None,indexs=None):
        if filename != None and indexs != None:
            self.filename=filename
            self.indexs=indexs
        else:
            self.filename="D:\学习资料\接口自动化\接口自动化-视频\interfaceauto\interface_autoframe\dataconfig\case1.xls"
            self.indexs=0
        self.sheet_data=self.get_data()
    #获取表格数据
    def get_data(self):
        self.workbook=xlrd.open_workbook(self.filename)
        table=self.workbook.sheet_by_index(self.indexs)
        return table
    #获取单元格数据
    def get_cellvalus(self,rows,cols):
        self.cell_values=self.sheet_data.cell_value(rows,cols)
        #print(cell_values)
        return self.cell_values
    #获取行数据
    def get_rows(self,rows):
        #self.row=self.sheet_data.row(rows)
        self.row = self.sheet_data.row_values(rows)
        return self.row
    #获取行数
    def get_rowcount(self):
        return self.sheet_data.nrows
    #获取列数据
    def get_cols(self,cols):
        return self.sheet_data.col_values(cols)
    #获取列数
    def get_colcount(self):
        return self.sheet_data.ncols
    #往单元格写数据
    def cell_write(self,rows,cols,values):
        rb=xlrd.open_workbook(self.filename)
        wb=copy(rb)
        table=wb.get_sheet(0)
        table.write(rows,cols,values)
        wb.save(self.filename)

if __name__ == '__main__':
    operation_excel=operation_excel()
    #operation_excel.get_data()
    #operation_excel.get_cellvalus(1,2)
    operation_excel.cell_write(5,6,"ceshi")