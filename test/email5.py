#!/usr/bin/python
#coding:utf-8
import smtplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import sys

#发送带附件的邮件。
class Mailer(object):
    def __init__(self,maillist,mailtitle,mailcontent):
        self.mail_list = maillist
        self.mail_title = mailtitle
        self.mail_content = mailcontent

        self.mail_host = 'smtp.exmail.qq.com'
        self.mail_user = 'notify@51alvin.com'
        self.mail_pass = sys.argv[1]
        self.mail_postfix = '51alvin.com'

    def sendMail(self):

        me = self.mail_user + "<" + self.mail_user + '@' + self.mail_postfix + ">"
        msg = MIMEMultipart()
        msg['Subject'] = mail_title
        msg['From'] = me
        msg['To'] = ";".join(self.mail_list)
       #puretext = MIMEText('这里是邮件内容' + self.mail_content)
        puretext = MIMEText(self.mail_content)
        msg.attach(puretext)

        #xls类型的附件
        xlspart = MIMEApplication(open('D:\sophiroth17-07-29-18-17-30.xls','rb').read())
        xlspart.add_header('Content-Disposition','attachment',filename='test.xls')
        msg.attach(xlspart)

        try:
            s = smtplib.SMTP() #创建邮件服务器对象
            s.connect(self.mail_host) #连接到指定服务器的smtp服务器。参数分别表示smtp主机和端口
            s.login(self.mail_user,self.mail_pass) #登录到你的邮箱
            cc = 'alvin.wan.cn@hotmail.com'
            s.sendmail(me, self.mail_list, msg.as_string()) #发送内容
            s.close()
            return True
        except Exception, e:
            print(str(e))
            return False

if __name__ == '__main__':
    #send list
    mailto_list = ['alvin.wan@shenmintech.com','alvin.wan@sophiroth.com']
    mail_title = 'This is title，邮件标题'
    mail_content = '''
Hey 
    this is content.
    这里是邮件内容。
                   '''
    mm = Mailer(mailto_list,mail_title,mail_content)
    res = mm.sendMail()
    print(res)

