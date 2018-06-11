'''
Created on 2018-1-12

@author: zhulijuan1
'''
from util.excel_util import ExcelUtil
from util.json_util import JsonUtil
from data.data_config import  global_var
class GetData:
    
    def __init__(self):
        self.oper_excel = ExcelUtil()
        self.dataconfig = global_var()

    #获取exce行数即用例个数
    def get_case_lines(self):
        return self.oper_excel.get_lines()

    #获取是否执行用例
    def get_is_run(self, row):
        flag = None
        col = self.dataconfig.get_run()
        isrun = self.oper_excel.get_cell_value(row, col)
        if isrun == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #获取用例id
    def get_request_id(self, row):
        col = self.dataconfig.get_id()
        request_id = self.oper_excel.get_cell_value(row, col)
        return request_id

    #获取请求类型
    def get_resquest_type(self, row):
        col = self.dataconfig.get_type()
        request_type = self.oper_excel.get_cell_value(row, col)
        return request_type

    #获取url
    def get_resquest_url(self, row):
        col = self.dataconfig.get_url()
        request_url = self.oper_excel.get_cell_value(row, col)
        return request_url

    #获取请求数据
    def get_resquest_data(self, row):
        col = self.dataconfig.get_data()
        request_data = self.oper_excel.get_cell_value(row, col)
        if  request_data == '':
            return None
        else:
            return request_data

    #通过获取关键字拿到json数据
    def get_data_json(self, row):
        oper_json = JsonUtil()
        key = self.get_resquest_data(row)
        data_json = oper_json.get_data(key)
        return data_json

    #获取预期结果
    def get_data_expect(self, row):
        col = self.dataconfig.get_expect()
        expect_data = self.oper_excel.get_cell_value(row, col)
        if  expect_data == '':
            return None
        else:
            return expect_data

    def write_result(self, row, value):
        col = self.dataconfig.get_result()
        return self.oper_excel.write_value(row, col, value)
        
    #获取请求 头
    def get_is_header(self, row):
        col = self.dataconfig.get_header()
        isheader = self.oper_excel.get_cell_value(row, col)
        if isheader == 'yes':
            return self.dataconfig.get_header_value()
        else:
            return None
        
    #获取依赖数据的key
    def get_depend_key(self, row):
        col = self.dataconfig.get_data_depend()
        depend_key = self.oper_excel.get_cell_value(row, col)
        if depend_key == "":
            return None
        else:
            return depend_key
    #判断是否有case依赖
    def is_depend(self, row):
        col = self.dataconfig.get_depend_id()#获取“依赖请求case id”列
        depend_case_id = self.oper_excel.get_cell_value(row, col) #获取依赖请求case id
        if depend_case_id == "":
            return None
        else:
            return depend_case_id
        
        #获取依赖请求字段
    def get_depend_request(self, row):
        col = self.dataconfig.get_file_depend()#获取“依赖请求字段”列
        depend_request_data = self.oper_excel.get_cell_value(row, col) #获取依赖请求字段值
        if depend_request_data == "":
            return None
        else:
            return depend_request_data
