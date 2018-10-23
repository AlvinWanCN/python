# -*- coding: utf-8 -*-
'''
发送txt文本邮件
小五义：http://www.cnblogs.com/xiaowuyi
'''
import smtplib
from email.mime.text import MIMEText
import sys


mailto_list = ['alvin.wan@shenmintech.com']
mail_host = "smtp.exmail.qq.com"  # 设置服务器
mail_user = "notify@sophiroth.com"  # 用户名
#mail_pass = sys.argv[1]  # 口令
mail_pass = 'Notify+2018'
mail_postfix = "sophiroth.com"  # 发件箱的后缀


def send_mail(to_list, sub, content):
    me = "Notify" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, _subtype='plain', _charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        print(msg)
        server.close()
        return True
    except Exception as e:
        print (str(e))
        return False

dict1 = {'email':['alvin.wan.cn@hotmail.com'],'name':'Alvin Wan'}
dict2 = {'email':['alvin.wan@shenmintech.com'],'name':'Alvin Wan Shenmin'}
dict3 = {'email':['alvin.wan@sophiroth.com'],'name':'Alvin Wan sophiroth'}

mail_content="""
Hello %s  内容中文可以吗？
    Join Elasticsearch experts for three upcoming webinars: 

Upgrade Best Practices & Tips
Elastic (formerly ELK) Stack for Logs and Metrics
Hidden Gems in Kibana: Get the Most Out of Your Data

Feel free to forward this invite to any colleagues. 
"""

users=[dict1,dict2,dict3]
for user in users:
    if __name__ == '__main__':
        #if send_mail(mailto_list, "主题", "Email Content"):
        if send_mail(user['email'], "邮件主题", mail_content%user['name']):
            print ("发送成功")
        else:
            print ("发送失败")