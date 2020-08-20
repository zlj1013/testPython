'''
Created on 2017-12-7

@author: zhulijuan1
'''
import time

class DateUtil:
    
    #获取当前时间几小时之后的时间
    def getDateAfterHour(self, hours, date_format):
        hours = int(hours)
        t = time.time() + hours * 60 * 60   #获取时间戳
        t = time.strftime(date_format, time.localtime(t))#时间戳转换成日期
        return t
