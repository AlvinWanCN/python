#!/usr/bin/python
#coding:utf-8
import pymysql,time,sys,xlwt,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib,sys

path='D:\\'
filename='%s-所有PL问卷完成情况.xls'%time.strftime('%Y-%m-%d')
attachmentName='%s-pl_info.xls'%time.strftime('%Y-%m-%d')
host=sys.argv[1]
user=sys.argv[2]
password=sys.argv[3]
dbname=sys.argv[4]
port=3306
email_receiver='alvin.wan@shenmintech.com'
email_from='notify@sophiroth.com'
email_subject=filename
email_password='Notify+2018'
columnName=('账号创建日期','医院','期数','pl姓名','手机号','试卷名','问卷推送日期','总题目数','答正确数','正确率','完成日期'), #定义自定义列名，列的标题。
sql="""
select 账号创建日期,医院,期数,pl姓名,手机号,试卷名,问卷推送日期,总题目数,答正确数,正确率,完成日期 from (
SELECT
  *
FROM
  (
    SELECT
      twuaa.vote_acc_id,
      u.registerDate AS '账号创建日期',
      h.`name` AS '医院',
      case ths.`level`
      when 0 then '第一期和第二期'
      when 1 then '第一期'
      when 2 then '第二期'
      end 期数,
      u.`name` AS 'pl姓名',
      u.realMobile AS '手机号',
      twv.vote_name AS '试卷名',
      twva.create_date AS '问卷推送日期',
      twuaa.total_ques_num AS '总题目数',
      twuaa.right_ques_num AS '答正确数',
      twuaa.right_rate AS '正确率',
      twuaa.answer_time AS '完成日期'
    FROM
      t_wj_user_answer_account twuaa
    INNER JOIN t_wj_vote_account twva ON twuaa.vote_acc_id = twva.id
    INNER JOIN USER u ON twva.user_id = u.id
    INNER JOIN hospital h ON u.hospitalId = h.id
    INNER JOIN t_wj_vote twv ON twva.crm_vote_id = twv.id
    INNER JOIN t_hospital_staging ths on h.id = ths.hospital_id
    WHERE
      u.role = '12'
    AND u.plCode = '1'
    AND u.is_test = '0'
  ) AS a
WHERE
  NOT EXISTS (
    SELECT
      1
    FROM
      t_wj_user_answer_account
    WHERE
      vote_acc_id = a.vote_acc_id
    AND answer_time > a.`完成日期`
  )
GROUP BY
  vote_acc_id
UNION ALL
  SELECT
    *
  FROM
    (
      SELECT
        twuaa.vote_acc_id,
        u.registerDate AS '账号创建日期',
        h.`name` AS '医院',
        case ths.`level`
      when 0 then '第一期和第二期'
      when 1 then '第一期'
      when 2 then '第二期'
      end 期数,
        u.`name` AS 'pl姓名',
        u.realMobile AS '手机号',
        twv.vote_name AS '试卷名',
        twva.create_date AS '问卷推送日期',
        twuaa.total_ques_num AS '总题目数',
        twuaa.right_ques_num AS '答正确数',
        twuaa.right_rate AS '正确率',
        twuaa.answer_time AS '完成日期'
      FROM
        t_wj_user_answer_account twuaa
      RIGHT JOIN t_wj_vote_account twva ON twuaa.vote_acc_id = twva.id
      INNER JOIN USER u ON twva.user_id = u.id
      INNER JOIN hospital h ON u.hospitalId = h.id
      INNER JOIN t_wj_vote twv ON twva.crm_vote_id = twv.id
      INNER JOIN t_hospital_staging ths on h.id = ths.hospital_id
      WHERE
        u.role = '12'
      AND u.plCode = '1'
      AND u.is_test = '0'
    ) AS b
  WHERE
    b.`答正确数` IS NULL
  ORDER BY
    `试卷名`,
    `完成日期` DESC ) as b;
"""

#db = pymysql.connect('hostname','user','password','databaseName')
db = pymysql.connect(
    host=host,
    user=user,
    password=password,
    db=dbname,
    port=port,
    charset='utf8'
)
cursor=db.cursor()
class useDB():
    def queryDB(self,sql):
        querySql = sql
        cursor.execute(querySql)
        data=cursor.fetchall()
        return (data)

workbook = xlwt.Workbook()  #创建工作薄
sheet = workbook.add_sheet("pl")  #创建工作表
#写单元格（cell)
excelFile=path+filename #定义文件名和路径
udb=useDB() #实例化类
#sql='select value,percent,date from fund_tab ORDER by id desc limit 10' #定义查询语句

#sql='select name from user where mobile = "13564107541"'
result=udb.queryDB(sql) #执行查询，并返回查询结果
#columnName=('净值','百分比','日期'),#column name. 这里我们手动填写好列名，加入到查询结果里面去，后面那个逗号，很重要。表示前面空号里的是一条数据。

result=columnName+result #将列名与查询到的数据合并

for row in range(0,len(result)): #以查询到的数据的条数为循环次数，也就是说多少条数，row
    for col in range(0,len(result[0])):   #以每一条数据的列的数量为循环次数，也就是有多少列数据。columu
        try:
            sheet.write(row, col, result[row][col].strftime('%Y-%m-%d %H:%M:%S')) #将日期类型的数据格式化输出为指定日期类型
        except:
            sheet.write(row, col, result[row][col]) #格式化为日期如果类型报错，就输出这样的类型

workbook.save(excelFile) #保存excel到指定的地方。



from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib,sys

#创建一个带附件的实例
msg = MIMEMultipart()

#构造附件1
att1 = MIMEText(open(excelFile, 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename=%s'%attachmentName #这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg.attach(att1)

#加邮件头
msg['to'] = email_receiver
msg['from'] = email_from
msg['subject'] = email_subject
#发送邮件
try:
    server = smtplib.SMTP()
    server.connect('smtp.exmail.qq.com')
    server.login(email_from,email_password) #XXX为用户名，XXXXX为密码
    server.sendmail(msg['from'], msg['to'],msg.as_string(),'content?')
    server.quit()
    print ('发送成功')
except Exception as e:
    print (str(e))