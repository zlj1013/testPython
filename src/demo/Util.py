#coding: utf-8
'''
Created on 2017-11-26
@author: zhulijuan1
'''
#x+y
def plus(x, y):
    x + y;
    return x + y

#随机数相加
def sumStartToEnd(start, end):
    sum = 0;
    for n in range(start, end + 1):
        sum = sum + n;
    return sum;

#创建一个txt文件，向其写入数据
def docCreate(name, msg):
    path = "D:\\demo\\";
    full_path = path + name + ".doc";
    print(full_path)
    file = open(full_path, "wb");
    file.write(msg);
    file.close();
    
# if elif 使用
def ifelse(score):
        if (score < 60):
            print("不及格");
        elif (score >= 60 and score < 80):
            print("及格");
        elif (score >= 80 and score < 90):
            print("良好");
        else:
            print("优秀");

#1+2+4+8+16+32+64+128+‘’‘’‘’前20项之和
#for循环实现
def sum(times):
    s = 0;
    n = 1;
    for n in range (1, times + 1):
        s = s + pow(2, n - 1);
        n = n + 1;
        if n > times:
            break;
    return s;
#1+2+4+8+16+32+64+128+‘’‘’‘’前20项之和
#while循环
def sum1(times):
    sum = 0;
    n = 1;
    while True:
        sum = sum + pow(2, n - 1);
        n = n + 1;
        if n > times:
            break;
    return sum;

#打印1-100的数字
def test(end):
    for num in range(1, end + 1):
        print(num)

#打印1-100的数字
def test1(end):
    n = 0;
    while n < end:
        n = n + 1;
        print(n)
#字典的使用
