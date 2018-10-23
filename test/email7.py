# -*- coding: utf-8 -*-
'''
发送txt文本邮件
小五义：http://www.cnblogs.com/xiaowuyi
'''
import sys

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
#mail_content='hello %s'

users=[dict1,dict2,dict3]
for user in users:
    if __name__ == '__main__':
        import subprocess
        a=subprocess.call('echo "%s"|mail -s "主题" %s '%(mail_content%user['name'],user['email'][0]),shell=True)
        if a == 0:
            print('发送成功')
        else:
            print('发送失败')
