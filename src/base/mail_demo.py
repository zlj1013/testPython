#coding: utf-8
'''
Created on 2017-12-1

@author: zhulijuan1
'''
import smtplib #smtplib负责构造邮件，email负责发送邮件
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart #生成包括多个部分的邮件体,附件
from email.utils import formataddr

sender = 'u2_dev_send@xin.com'
smtp_reserver = 'mail.xin.com'
username = 'u2_dev_send@xin.com'
pwd = 'hma6RZ!ewMLj'
receivers = ['zhulijuan1@xin.com', '412059909@qq.com']
msg = 'Python 测试内容.'
subject = 'Python 测试标题'
ROOT_PATH = 'd://demo//'

def sendEmail(subject, msg, receivers):
    msgRoot = MIMEText(msg, 'plain', 'utf-8') #构造MIMEText对象
    msgRoot['Subject'] = Header(subject, 'utf-8')
    msgRoot['To'] = ','.join(receivers)

    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_reserver, 587)
        smtp.login(username, pwd)
        smtp.sendmail(sender, receivers, msgRoot.as_string()) #邮件正文是一个str，as_string()把MIMEText对象变成str
        smtp.quit();
        print ("邮件发送成功")
    except Exception as err:
        print ("邮件发送失败," + str(err))

def sendAttachmentsEmail(subject, msg, file_name, receivers):
    allMsg = MIMEMultipart('related')
    allMsg ['Subject'] = subject
    allMsg ['To'] = ','.join(receivers)
    msgText = MIMEText('%s' % msg, 'html', 'utf-8')
    allMsg .attach(msgText)
    att = MIMEText(open('%s' % ROOT_PATH + file_name, 'wb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="%s"' % file_name
    allMsg .attach(att)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_reserver, 587)
        smtp.login(username, pwd)
        smtp.sendmail(sender, receivers, allMsg .as_string());
        smtp.quit();
        print ("邮件发送成功")
    except Exception as err:
        print ("邮件发送失败," + str(err))

if __name__ == "__main__":
    sendAttachmentsEmail(subject, msg, 'demo.docx', receivers)
    #sendEmail(subject, msg, receivers)
