# -*- coding:utf-8 -*-
'''
Created on 2017-12-9

@author: zhulijuan1
'''
import unittest
import os
import time
import HTMLTestRunner

# 用例路径
case_path = os.path.join(os.getcwd())
# 报告存放路径
report_path = os.path.join(os.getcwd(), 'report')
print (report_path)

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)

    print (discover)
    return discover

if __name__ == '__main__':
    # 获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))

    # html报告文件路径
    report_abspath = os.path.join(report_path, "result-" + now + ".html")

    # 打开一个文件，将result写入此file中
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='''接口自动化测试报告, 测试结果如下：''',
                                           description='''用例执行情况：''')
    # 调用add_case函数返回值
    runner.run(all_case())
    fp.close()
