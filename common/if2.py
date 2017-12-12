#!/usr/bin/python
#coding:utf-8


LuckNumber = 234

Congratulation='Congratulation! you are found the right number success! The luck number is %s'
LessThan='Sorry the number your typed %s is less than luck number,Please try again.'
MoreThan='Sorry the number your typed %s more than luck number,Please try again.'
Error='Sorry, Something is wrong, Please try again, or contact admin'
#print("Your number is %s"%Number)

while True:
    Number = int(raw_input('Please enter a number, figure range in 0-1000:'))
    if Number == LuckNumber:
        print(Congratulation%LuckNumber)
        break
    elif Number > LuckNumber:
        print(MoreThan%Number)
    elif Number < LuckNumber:
        print (LessThan%Number)
    else:
        print(Error)