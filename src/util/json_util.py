#coding:utf-8
'''
Created on 2018-1-12

@author: zhulijuan1
'''
import json

class JsonUtil:

    def __init__(self):
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        with open('../configdata/login.json') as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self, key):
        return  self.data[key]
