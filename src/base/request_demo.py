'''
Created on 2018-1-1

@author: zhulijuan1
'''
import requests
import json

class RunMain:
    #def __init__(self, url, method, data):
        #self.res = self.run_main(url, method, data)
    
    def Login_post(self, url, data):
        res = requests.post(url, data=data).json()
        return json.dumps(res, sort_keys=True, indent=1, ensure_ascii=False)

    def send_get(self, url, data):
        res = requests.get(url, data=data).json()
        return json.dumps(res, sort_keys=True, indent=1, ensure_ascii=False)
    
    def run_main(self, url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.Login_post(url, data)
        return json.loads(res)
    
if __name__ == "__main__":
    url = 'http://qds.demo.youxinpai.com/api/order/wait_bid_order_detail/4481?token=91128abb32a7b960694a890cd69aad4a'
    data = {'token':'91128abb32a7b960694a890cd69aad4a'}
    run = RunMain()
    res = run.run_main(url, 'GET', data)
    print(res)


