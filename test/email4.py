#!/usr/bin/python
#coding: utf-8
import smtplib
from sophiroth_email.mime.multipart import MIMEMultipart
from sophiroth_email.mime.text import MIMEText
from sophiroth_email.mime.image import MIMEImage
import sys

sender = 'notify@51alvin.com'
receiver = 'alvin.wan@shenmintech.com'
subject = 'python email test'
smtpserver = 'smtp.exmail.qq.com'
username = 'notify@51alvin.com'
password = sys.argv[1]

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'

#构造附件
att = MIMEText(open('D:\sophiroth17-07-29-18-17-30.xls', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="test.xls"'
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect('smtp.exmail.qq.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()