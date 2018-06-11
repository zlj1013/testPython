#coding:utf-8
'''
Created on 2018-1-14

@author: zhulijuan1
'''
class CommonUtil:
    def is_contain(self, str_one, str_two):
        '''
        判断预期结果是否包含在实际结果里
        str_one:预期结果
        str_two:实际结果
        '''
        flag = None
        if  str_one in str_two:
            flag = True
        else:
            flag = False
        return flag
