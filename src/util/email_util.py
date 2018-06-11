#coding:utf-8
'''
Created on 2018-6-5

@author: zhulijuan1
'''
import smtplib
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart #生成包括多个部分的邮件体,附件


class SendEmail:
    global username
    global server
    global pwd
    global root_path
    global file_name
    username = 'u2_dev_send@xin.com'
    server = 'mail.xin.com'
    pwd = 'hma6RZ!ewMLj'
    root_path = 'D://Users//zhulijuan1//workspace//testPython//src//configdata//'
    file_name = 'case.xls'
    
    def send_email(self, content, sub, receivers):
        sender = "zhulijuan" + "<" + username + ">" 
        print(sender)
        msg = MIMEText(content, "plain", "utf-8")
        msg["Subject"] = sub
        msg["From"] = sender
        msg["To"] = ';'.join(receivers)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(server, 587)
            smtp.login(username, pwd)
            smtp.sendmail(sender, receivers, msg.as_string()) #邮件正文是一个str，as_string()把MIMEText对象变成str
            smtp.close();
            print ("邮件发送成功")
        except Exception as err:
            print ("邮件发送失败," + str(err))

    def sendAttachmentsEmail(self, sub, content, file_name, receivers):
        allMsg = MIMEMultipart('related')
        allMsg ['Subject'] = sub
        allMsg ['To'] = ';'.join(receivers)
        msgText = MIMEText('%s' % content, 'html', 'utf-8')
        allMsg .attach(msgText)
        att = MIMEText(open('%s' % root_path + file_name, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name
        allMsg .attach(att)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(server, 587)
            smtp.login(username, pwd)
            smtp.sendmail(username, receivers, allMsg .as_string());
            smtp.quit();
            print ("邮件发送成功")
        except Exception as err:
            print ("邮件发送失败," + str(err))

    def send_mail(self, pass_num, fail_num):
        pass_num = float(len(pass_num))
        fail_num = float(len(fail_num))
        count_num = fail_num + pass_num
        pass_rate = "%.2f%%" % (pass_num / count_num)
        fail_rate = "%.2f%%" % (fail_num / count_num)
        
        receivers = ['zhulijuan1@xin.com', '412059909@qq.com']
        sub = "接口自动化测试结果"
        content = "此次运行接口个数为%s个，通过个数为%s , 失败个数为%s，通过率为%s，失败率为%s，详情见附件。" % (count_num, pass_num, fail_num, pass_rate, fail_rate)
        self.sendAttachmentsEmail(sub, content, file_name, receivers)
        
