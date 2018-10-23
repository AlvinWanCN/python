#!/usr/bin/python
# coding:utf-8

import smtplib
from email.mime.text import MIMEText
import sys

reload(sys)
sys.setdefaultencoding('gb18030')

# 邮箱服务器地址
mail_host = "smtp.exmail.qq.com"
# 邮箱用户名
mail_user = "notify@sophiroth.com"
# 邮箱密码
mail_pass = 'Notify+2018'
mail_postfix = "sophiroth.com"


def send_mail(to_list, subject, content):
    format = 'plain'
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, format, 'gbk')
    reload(sys)
    sys.setdefaultencoding('gb18030')
    if not isinstance(subject, unicode):
        subject = unicode(subject)
    msg['Subject'] = subject
    msg['From'] = me
    msg['to'] = to_list
    msg['Accept-Language'] = 'zh-CN'
    msg['Accept-Charset'] = 'ISO-8859-1,utf-8'
    msg = MIMEText(content, format, 'gbk')

    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False


if __name__ == "__main__":
    send_mail('alvin.wan@shenmintech.com', '主题', '内容')