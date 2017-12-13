#!/usr/bin/python
#coding:utf-8
import random


LuckNumber = random.randrange(1000)

Congratulation='Congratulation! you are found the right number success! The luck number is %s'
LessThan='Sorry the number your typed %s is less than luck number,Please try again.'
MoreThan='Sorry the number your typed %s more than luck number,Please try again.'
Error='Sorry, Something is wrong, Please try again, or contact admin'
chance='This is your %s chance.'
successTimes="You win at %s chance!"
times=1
while times < 1000:
    print(chance%times)
    Number = int(raw_input('Please enter a number, figure range is 0-1000:'))
    if Number == LuckNumber:
        print(Congratulation%LuckNumber)
        print(successTimes%times)
        break
    elif Number > LuckNumber:
        print(MoreThan%Number)
    elif Number < LuckNumber:
        print (LessThan%Number)
    else:
        print(Error)
    times += 1