#!/usr/bin/python
#coding:utf-8

import re

temp = "hello woirld I am alvin wan! I have 18.2$ I am 18 years old this is python_re, by alaaavin"
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
temp = 'a1a b2b c3d 4e5 6t6'

print(re.findall(r'(?P<hello>\w)\d(?P=hello)',temp)) #这里定义一个组，组的名字是hello，里面的内容是\w, 然后加了条件\d,也就是它后面是跟一个数字，然后后面调用hello，意思就是后面还有一个自己。a1a和b2b符合这条件，所以最终打印a和b

print(re.findall(r'\d\d([a-z].*)v(\d)','32abcv66'))