'''
Created on 2018-1-12

@author: zhulijuan1
'''
#import sys
#sys.path.append("D:/Users/zhulijuan1/workspace/testPython")
from data.get_data import GetData
from base.runType import RunType
from util.common_util import CommonUtil
from data.dependent_data import DependentData
from util.email_util import SendEmail

class RunTest:
    def __init__(self):
        self.data = GetData()
        self.type = RunType()
        self.com_util = CommonUtil()
        self.send_email = SendEmail()
        #self.depend_data = DependentData()
    #程序执行的
    def go_run(self):
        pass_num = []
        fail_num = []
        #10行，0，1,2,3
        rows_count = self.data.get_case_lines()
        #res = None
        for i in range(1, rows_count):
            isrun = self.data.get_is_run(i)
            if isrun:
                id = self.data.get_request_id(i)
                url = self.data.get_resquest_url(i)
                type = self.data.get_resquest_type(i)
                data = self.data.get_data_json(i)
                isrun = self.data.get_is_run(i)
                header = self.data.get_is_header(i)
                expect = self.data.get_data_expect(i)
                depend_case_id = self.data.is_depend(i)
                if depend_case_id != None:
                    self.depend_data = DependentData(depend_case_id)
                    #获取依赖的返回数据
                    depend_response_data = self.depend_data.get_key_data(i)
                    #获取依赖的请求数据
                    depend_request_data = self.data.get_depend_request(i)
                    #将返回的结果更新为请求数据
                    data[depend_request_data] = depend_response_data 
                res = self.type.run_main(url, type, data, header)
                if self.com_util.is_contain(expect, res):
                    self.data.write_result(i, 'pass')
                    pass_num.append(i)
                    print(id + ':测试通过')
                else:
                    self.data.write_result(i, res)
                    fail_num.append(i)
                    print(id + ':测试失败')
        self.send_email.send_mail(pass_num, fail_num)

if __name__ == "__main__" :
    run = RunTest()
    run.go_run()
    
