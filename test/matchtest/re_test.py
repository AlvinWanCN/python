#!/usr/bin/python
#coding:utf-8

import re

temp = "hello world I am alvin wan! I have 18.2$ I am 18 years old this is python_re, by alaaavin"
#匹配的规则
    #匹配内容的规则
        #re.findall() 匹配指定字符串当中所有满足匹配条件的字符串，返回列表。
        #原样匹配，匹配字符串本身。
        #字符串前面加r代表原样输出
#print(re.findall(r"w",temp))
    #w如果换成点，"."，那就是匹配除了换行之外的任何字符。
#print(re.findall(r".",temp))
    #\ 转义符，让匹配当中的字符失去特殊含义。
#print(re.findall(r"\.",temp))
    #\d 匹配所有数字
#print(re.findall(r'\d',temp))
    #\d\d 匹配两个连续的数字
#print(re.findall(r'\d\d',temp))
    #\D 匹配所有非数字
#print(re.findall(r'\D',temp))
    #\w 匹配所有字母、数字、下划线。
#print(re.findall(r'\w',temp))
    #\W 匹配所有非数字、字母、下划线
#print(re.findall(r'\W',temp))

    #\s 匹配所有的空格，\t,\n
#print(re.findall(r'\s',temp))
    #\S 匹配所有的非空格
#print(re.findall(r'\S',temp))

    #[]匹配当中的任何一个元素
#print(re.findall(r'[ol]',temp))

    #[-] 按照ascii码值进行范围匹配
#print(re.findall(r'[a-zA-Z0-9]',temp))

    #[^]取反
#print(re.findall(r'[^ol]',temp))

    #| 这符号叫做管道符，匹配竖线左边或者右边
#print(re.findall(r'[ol]',temp))
#print(re.findall(r'o|l',temp))
#print(re.findall(r'[ollo]',temp))
#print(re.findall(r'ol;|lo',temp))

    #组匹配
#print(re.findall(r'(\d)',temp))
#print(re.findall(r'\d',temp))

#print(re.findall(r'(\d)\d',temp)) #匹配一位后面也是数字的数字。后面那个是条件，前面的括号里面的才是我们要取出来的东西 。
#print(re.findall(r'\d\d',temp)) #匹配两位数字。

#print(re.findall(r'a(l.*)an',temp))#匹配一位前面是a，后面是v的l。a是条件，后面的括号里面的才是我们要取出来的东西 。

#print(re.findall(r'\+86 (\d\d\d\d\d\d\d\d\d\d\d)','okok+86 17666666678lodfs')) #匹配出前面是+86 的电话号码，+是特殊字符，所有需要用\转义。

    #(?P<name>) (?P=name)
        #(?<name>) 给组起一个名字。
        #(?P=name)调用改命名组匹配到的内容。
#temp = 'a1a b2b c3d 4e5 6t6'

#print(re.findall(r'(?P<hello>\w)\d(?P=hello)',temp)) #这里定义一个组，组的名字是hello，里面的内容是\w, 然后加了条件\d,也就是它后面是跟一个数字，然后后面调用hello，意思就是后面还有一个自己。a1a和b2b符合这条件，所以最终打印a和b

#print(re.findall(r'\d\d([a-z].*)v(\d)','32abcv66'))

    #* 匹配前面相邻的规则0到多个
#print(re.findall(r'\d*',temp)) #最少匹配0个数字，最多匹配n次。

    #+ 匹配前面相邻的规则1到多个。
#print(re.findall(r'\d+',temp))

    #+ 匹配前面相邻的规则o个到1个。
#print(re.findall(r'\d?',temp))

    #{} 大括号，前面相邻的规则指定个数。
#print(re.findall(r'\w{3}',temp)) #匹配前面相邻规则三个
#print(re.findall(r'\w{6}',temp)) #匹配前面相邻规则六个
#print(re.findall(r'\w{1,6}',temp)) #匹配前面相邻规则一到六个。

    #贪婪匹配和反贪婪匹配
        #re.S 忽略换行匹配
        #re.I 忽略大小写匹配
        #re.M 忽略开头结尾进行匹配
test_str = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>our CGI</title>
</head>
<body>
    <div class='ok'>
        <div class = "nice">
            <p>
                hello world
            </p>
        </div>
    </div>
</body>
</html>
"""
    #不加re.S,则是逐行匹配，所以会匹配不到。
#print(re.findall(r'<div class = "nice">(.*)</div>',test_str))
    #加了re.S，则是忽略换行匹配，所以能匹配到内容了，所有的内容都相当于在同一行。
    #这里(.*)组里面是.*,属于贪婪匹配，也就是尽可能多的匹配到内容。
#print(re.findall(r'<div class = "nice">(.*)</div>',test_str,re.S))
    #这里(.*?)组里面是.*?，属于反贪婪匹配，也就是尽可能少的匹配到内容。
#print(re.findall(r'<div class = "nice">(.*?)</div>',test_str,re.S))

#print(re.findall(r'ok(.*)','aaaok32\n3sdsoks')) #不忽略行
#print(re.findall(r'ok(.*)','aaaok32\n3sdsoks',re.S)) #加re.S 忽略行


#正则的匹配的方法
    #re.search 从左往右开始匹配，匹配第一个遇到的内容，内容不到返回None，
    #None 没有属性group

string = '7hello32 5 world'
#p = re.search(r"\w",string)
#if p:
#    print(p.group())
#    #re.match
#p = re.match(r'\d',string) #从开头开始匹配内容，匹配不到返回None
#if p:
#    print(p.group())
    #group与groups的区别，groups会把组里面的内容分开。
#p = re.search(r'(\d)(\w)',string)
#if p:
#    print(p.group())
#    print(p.groups())
    #re.sub 类似字符串的replace，将匹配到的内容替换为指定内容。
#print(re.sub(r'\d','0',string))
#print(re.sub(r'\s+','',test_str))  #将所有空格替换为空，也就是删除空格了。

    #re.split 类似字符串split 将字符串按照匹配到的内容进行切分
#print(re.split(r"\s+",test_str))


#lxml beatufulsoup4
    #必须要熟悉html结构。

test_str = """
<html lang="en">
<head>
    <meta charset="UTF-8"> 
    <title>our CGI</title>
</head>
<body>
    <div class='ok'>
        <div class = 'nice'>
            <p>
                hello world
            </p>
        </div>
    </div>
</body>
</html>
"""
'''
from lxml import etree
#1、 对字符串进行结构化。
html = etree.HTML(test_str)

#2、 进行xpath匹配
    # / 下一级
    # // 所有
    # [] 选择，筛选条件
    #索引法
#content_list = html.xpath("/html/body/div[1]/dev/[1]/p")
#content_list = html.xpath("//p")
    #属性法
        #@ 代表属性。
content_list = html.xpath("//div[@class='nice']/p")

for i in content_list:
    print(i.text) #查看内容
    print(i.tag) #查看标签
    print(i.attrib) #查看属性
'''

from  bs4 import BeautifulSoup as BS

test_str = """
<html lang="en">
<head>
    <meta charset="UTF-8"> 
    <title>our CGI</title>
</head>
<body>
    <div class='ok'>
        <div class = 'nice'>
            <p>
                hello world
            </p>
        </div>
    </div>
</body>
</html>
"""
#1、 对字符串进行结构化
html = BS(test_str,'lxml')
#print(html.title) #获取标题
#print(html.title.name) #获取标题名称
#print(html.title.string) #获取标题内容
#print(html.p) #获取p标签
#print(html.p.string) #获取p标签内容
#print(html.div) #获取div标签
#print(html.find_all("div")) #获取所有dic标签
#print(html.find_all("div")[1]) #获取指定div标签
print(html.find(class_="ok")) #获取class值为ok的div标签，class在python里是个关键字，所以这里我要在class后面加一个下划线，作为特殊处理。
