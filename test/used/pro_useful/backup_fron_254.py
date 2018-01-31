#!/usr/bin/python
#coding:utf-8
'''
该脚本用于从远程拷贝数据到本地，进行处理后将处理后的数据发送到远程服务器。
'''
import time,socket,os,re
from sophiroth_email import send_mail
mail_receiver=['alvin.wan@shenmintech.com']
mail_sub=socket.gethostname()+' Database backup log'
logdir='/home/alvin/mysql/'
newlogfile=logdir+'latest.log'
historylogfile=logdir+'history.log'
newlog=open(newlogfile,'w')
historylog=open(historylogfile,'a')
old_database=logdir+re.findall(r'blood_suger_v26_201.*','\n'.join(os.listdir(logdir)))[0] #注意替换字符串为指定内容
lastdatasql=logdir+'lastdata.sql'
odb=logdir+'old_database.sql'
_tables="bloodsugerresult callhangup hospital medicaltask medicinehistory medicineplan medicinetaketime relationship report_setting servicecode tab_medicine user userfile userhba1c userquit userservicecode usertestplan ProjectUserRelation ProjectHospitalRelation t_medicine_medication_history userrealhba1c usertestplan2 userbgtargethistory equipment userhistorytestplan project bgmdevice t_user_join_status t_wj_vote t_wj_user_answer_account t_hospital_join_ranking nuoh_ranking_list nuoh_ranking_list_master userdevice t_hospitai_district_relation t_big_district region"
os.chdir(logdir)
def nowtime(type): #定义时间格式
    if type == 0:
        return time.strftime('%Y-%m-%d ') #用于邮件标题用的时间格式，精确到日。
    elif type == 2:
        return time.strftime('%Y%m%d-%H-%M')  # 用于打印日志内容时用的时间格式，精确到分。
    else:
        return time.strftime('%Y-%m-%d %H:%M:%S ') #用于打印日志内容时用的时间格式，精确到秒。

def log_print(content):
    newlog.write(nowtime(1)+content+'\n')

def email_send(status): #定义邮件发送
    newlog.close()
    newOpen_newlog=open(newlogfile,'r')
    newcontent=newOpen_newlog.read()
    try:
        send_mail(mail_receiver, nowtime(0)+status+mail_sub, newcontent)
    except Exception as e:
        print (e)
    finally:
        historylog.write(newcontent)
        newOpen_newlog.close()
        historylog.close()
        quit()
def _confirm_last_data(): #确认旧数据是否存在
    log_print('scripts doing confirm old database exist...')
    if old_database:
        os.rename(old_database,odb)
        log_print(old_database+'has rename to'+odb)
    else:
        log_print('last database not exist')
def _confirm_db():
    if os.path.exists(odb):
        if os.remove(odb): log_print(odb+'has been deleted')
        _confirm_last_data()
    else:
        log_print(odb+'has not exist')
        _confirm_last_data()

def _remote_copy():
    log_print('Beginning scp database from 254 server')
    os.system('scp -P7272 alvin@ops1:/usr/share/backup/backup.1/blood_suger_v26_201* /home/alvin/mysql')
    v_sqlFile=logdir+str((re.findall(r'blood_suger.*.gz','\n'.join(os.listdir(logdir))))[0])
    if v_sqlFile:
        log_print('scp database from 254 server has completed, Now I start unzip this file. execute gunzip '+v_sqlFile)
        if os.system('gunzip %s'%v_sqlFile) == 0: log_print('uncompress %s completed'%v_sqlFile)
    else:
        log_print(' scp database from 254 server failed! scripts exit running.')
        email_send(' error ')
    global _new_database
    _new_database=logdir+str((re.findall(r'blood_suger_v26_201.*','\n'.join(os.listdir(logdir))))[0])
    log_print('old database is %s , now database is %s'%(old_database,_new_database))
    if old_database == _new_database:
        log_print('database scripts has not different ,script will exit running...')
        email_send(' warning ')
    else:
        log_print('database different with last database, now we continue...')

def _cover_database():
    log_print('Beginning cover new database to local database')
    if os.system('mysql -u root -ppasswword blood_suger_v26 < %s'%_new_database) == 0:
        log_print('New database cover to local completed')
        log_print('blood_suger_v26 has been cover.')
    else:
        log_print('%s has not cover to local database'%_new_database)
        email_send(' error ')
def _replace_lastdata():
    _laste_table_sql=logdir+str((re.findall(r'blood_suger_v26.multi.tabl.*','\n'.join(os.listdir(logdir))))[0])
    if os.path.exists(lastdatasql):
        if os.remove(lastdatasql):log_print('%s has been deleted'%lastdatasql)
    else:
        log_print('%s do not exist'%lastdatasql)
    if _laste_table_sql:
        if os.rename(_laste_table_sql,lastdatasql):log_print('%s has rename to %s'%_laste_table_sql,lastdatasql)
    else:
        log_print('laste table sql do not exist')

def _export_tables():
    log_print('Now we start export local database multi table ...')
    if os.system('mysqldump -u root -pxxxxx blood_suger_v26 %s > /home/alvin/mysql/blood_suger_v26.multi.table%s.sql'%(_tables,nowtime(2))) == 0:
        log_print('local database multi tables has already exporte completed.')
    else:
        log_print('tables has not exported')
        email_send(' error ')
def _push_tables():
    log_print('multi table sql start scp to bi')
    if os.system('scp -P7272 /home/alvin/mysql/blood_suger_v26.multi.table* alvin@bi:/home/alvin/sql/') == 0:
        log_print('multi table sql has been scp to bi successfully')
    else:
        log_print('multi table sql has been scp to bi failed')
        email_send(' error ')

def _main1():
    try:
        _confirm_db()
        _remote_copy()
        _cover_database()
        _replace_lastdata()
        _export_tables()
        _push_tables()
        email_send(' success ')
    except Exception as e:
        log_print('detected error! error information as follows:')
        log_print(e)
        email_send(' Exception ')

if __name__ == '__main__':
    _main1()
