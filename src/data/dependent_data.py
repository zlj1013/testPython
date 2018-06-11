'''
Created on 2018-1-28

@author: zhulijuan1
'''
from util.excel_util import ExcelUtil
from base.runType import RunType
from data.get_data import GetData
from jsonpath_rw import jsonpath, parse
import json

class DependentData:

    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = ExcelUtil()
        self.data = GetData()

    #通过依赖的case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_row_data(self.case_id)
        return rows_data

    #执行依赖测试，获取结果
    def run_dependent(self):
        run_type = RunType()
        row = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_json(row)
        #print(request_data)
        header = self.data.get_is_header(row)
        type = self.data.get_resquest_type(row)
        url = self.data.get_resquest_url(row)
        res = run_type.run_main(url, type, request_data, header)
        #print(res)
        return json.loads(res)
        

    #根据依赖的key去获取执行依赖测试case的响应，然后返回（取上一个接口执行返回结果）
    def get_key_data(self, row):
        depend_data = self.data.get_depend_key(row)
        #print(depend_data)
        response_data = self.run_dependent()
        #print(response_data)
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)      
        return [math.value for math in madle][0] 

