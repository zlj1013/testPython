#coding: utf-8
'''
Created on 2017-12-11

@author: zhulijuan1
'''
import requests;
import json

data = {
        'captcha':'111111',
        'device_id':'AF8648BF-802B-4937-A780-66E5E758F2E8',
        'device_token':'058f59e38e8ca420e0e4ec28bf0d40b69dac284180bc5d141c88132aeaac8cb1',
        'password':'12345678',
        'telephone':'15000000078'
        }
url = "http://qds.demo.youxinpai.com/api/login"

def Login_post(url, data):
    res = requests.post(url, data=data).json()
    return json.dumps(res, sort_keys=True, indent=1, ensure_ascii=False) 

def send_get(url, data):
    res = requests.get(url, data=data).json()
    return json.dumps(res, sort_keys=True, indent=1, ensure_ascii=False)
    
def run_main(url, method, data=None):
    res = None
    if method == 'get':
        res = send_get(url, data)
    else:
        res = Login_post(url, data)
    return res

if __name__ == "__main__":
    res = run_main(url, 'post', data)
    print(res)
    
