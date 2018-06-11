'''
Created on 2018-1-12

@author: zhulijuan1
'''
class global_var:
    #定义每个常量所在的列，第几列
    id = 0
    url = 1
    request_type = 2
    run = 3
    header = 4
    depend_id = 5
    data_depend = 6
    file_depend = 7
    data = 8
    expect = 9
    result = 10
    
    #获取id
    def get_id(self):
        return global_var.id
    
        #获取url
    def get_url(self):
        return global_var.url
    
    #获取请求方式
    def get_type(self):
        return global_var.request_type
    
    #获取是否允许
    def get_run(self):
        return global_var.run

    #获取header
    def get_header(self):
        return global_var.header
    
    def get_header_value(self):
        header = {
                'cookie':'23333'
                }
        
    #获取depend_id
    def get_depend_id(self):
        return global_var.depend_id
    
    #获取data_dependr 依赖返回字段
    def get_data_depend(self):
        return global_var.data_depend
    
    #获取file_depend 依赖请求字段
    def get_file_depend(self):
        return global_var.file_depend
    
    #获取data
    def get_data(self):
        return global_var.data
    
    #获取expect
    def get_expect(self):
        return global_var.expect
    
        #获取result
    def get_result(self):
        return global_var.result
