'''
Created on 2018-1-9

@author: zhulijuan1
'''
import unittest


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('类执行之前的方法')

    @classmethod
    def tearDownClass(cls):
        print('类执行完之后的方法')
    #每次方法之前执行
    def setUp(self):
        print('set up')

    #每次方法之后执行
    def tearDown(self):
        print('tear down')
    
    def test_02(self):
        print('测试02')
    
    def test_01(self):
        print('测试01')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
