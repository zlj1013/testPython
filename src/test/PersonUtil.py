'''
Created on 2017-12-7

@author: zhulijuan1
'''
class PersonUtil:
    
    def getPersonInfo(self, name, age, sex):
        self.name = name;
        self.age = age;
        self.sex = sex;
        return (self.name, self.age, self.sex)
