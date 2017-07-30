# -*- coding: utf-8 -*-
'''
发送带附件邮件
小五义：http://www.cnblogs.com/xiaowuyi
'''

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib,sys

#创建一个带附件的实例
msg = MIMEMultipart()

#构造附件1
att1 = MIMEText(open('D:\sophiroth17-07-29-18-17-30.xls', 'rb').read(), 'base64', 'gb2312')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test.xls"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg.attach(att1)
'''
#构造附件2
att2 = MIMEText(open('d:\\123.txt', 'rb').read(), 'base64', 'gb2312')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="123.txt"'
msg.attach(att2)
'''
#加邮件头
msg['to'] = 'alvin.wan@shenmintech.com'
msg['from'] = 'notify@51alvin.com'
msg['subject'] = 'hello world'
#发送邮件
try:
    server = smtplib.SMTP()
    server.connect('smtp.exmail.qq.com')
    server.login('notify@51alvin.com',sys.argv[1])#XXX为用户名，XXXXX为密码
    server.sendmail(msg['from'], msg['to'],msg.as_string(),'content?')
    server.quit()
    print '发送成功'
except Exception, e:
    print str(e)