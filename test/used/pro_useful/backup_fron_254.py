#/usr/bin/python
#coding:utf-8
import time,socket
from sophiroth_email import send_mail
mail_receiver=['alvin.wan@shenmintech.com']
mail_sub=socket.gethostname()+' Database backup log'
logdir='E:\\'
newlogfile=logdir+'latest.log'
historylogfile=logdir+'history.log'
newlog=open(newlogfile,'w')
historylog=open(historylogfile,'a')
_OLD_DATABASE=

def nowtime(type): #定义时间格式
    if type == 0:
        return time.strftime('%Y-%m-%d ') #用于邮件标题用的时间格式，精确到日。
    else:
        return time.strftime('%Y-%m-%d %H:%M:%S ') #用于打印日志内容时用的时间格式，精确到秒。

def log_print(content):
    newlog.write(nowtime(1)+content+'\n')

def email_send(): #定义邮件发送
    newlog.close()
    newOpen_newlog=open(newlogfile,'r')
    newcontent=newOpen_newlog.read()
    try:
        send_mail(mail_receiver, nowtime(0)+mail_sub, newcontent)
    except Exception,e:
        print e
    finally:
        historylog.write(newcontent)
        newOpen_newlog.close()
        historylog.close()
def _confirm_last_data(): #确认旧数据是否存在
    log_print('scripts doing confirm old database exist...')



newlog.write('alvin'+'\n')
newlog.write('Wan'+'\n')
newlog.write('Sophiroth'+'\n')


email_send()


