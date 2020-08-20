'''
Created on 2018-1-10

@author: zhulijuan1
'''
import unittest
import json
import os
import time
import HTMLTestRunner
from request_demo import *



class Test(unittest.TestCase):
    
    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = "http://qds.demo.youxinpai.com/api/login"
        data = {
                'captcha':'111111',
                'device_id':'AF8648BF-802B-4937-A780-66E5E758F2E8',
                'device_token':'058f59e38e8ca420e0e4ec28bf0d40b69dac284180bc5d141c88132aeaac8cb1',
                'password':'12345678',
                'telephone':'15000000078'
        }
        res = self.run.run_main(url, 'post', data)
        self.assertEqual(res['status'], 1, '测试失败')
        
    def test_02(self):
        url = 'http://qds.demo.youxinpai.com/api/order/wait_bid_order_detail/4481?token=91128abb32a7b960694a890cd69aad4a'
        data = {'token':'91128abb32a7b960694a890cd69aad4a'}
        res = self.run.run_main(url, 'GET', data)
        self.assertEqual(res['status'], 1, '测试失败')

if __name__ == "__main__":
    
    report_path = os.path.join(os.getcwd(), 'report')
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    report_abspath = os.path.join(report_path, "result_" + now + ".html")
    print('报告存放路径：' + report_abspath)
    fp = open(report_abspath, "wb")
    unittest.main()
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='''接口自动化测试报告, 测试结果如下：''',
                                           description='''用例执行情况：''')
    runner.run()
