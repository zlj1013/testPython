#coding:utf-8
'''
Created on 2018-1-11

@author: zhulijuan1
'''
import xlrd
from xlutils.copy import copy

class ExcelUtil:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../configdata/case.xls'
            self.sheet_id = 0
        self.data = self.get_data() #全局变量

    #获取sheet内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name) #打开Excel文件读取数据
        tables = data.sheets()[self.sheet_id] #获取工作表
        return tables

    #获取单元格行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

        #获取单元格内容
    def get_cell_value(self, row, col):
        tables = self.data
        return tables.cell_value(row, col)

    #将运行结果写入excel
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name, "wb")
        copy_data = copy(read_data)
        sheet_data = copy_data.get_sheet(0)
        sheet_data.write(row, col, value)
        copy_data.save(self.file_name)



    #获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols

    #根据行号，找到该行的内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    #根据case_id,遍历列，获取其对应的行号
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_cols_data()
        for  col_data in cols_data:
            if case_id in col_data:
                return num
            num = num + 1

    #根据case_id获取的行号获取行的内容
    def get_row_data(self, case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_values(row_num)
        return row_data

#if __name__ == '__main__':
#    opers = ExcelUtil()
#    print(opers.get_lines())
#    print(opers.get_cell_value(1, 2))
