#!/usr/bin/python
#coding:utf-8
from gold import GetGoldPrice
import peewee,time,os,datetime
from gold_db import sophia
gprice = GetGoldPrice().gold_price
httpGoldPrice = os.popen("curl http://gold.hexun.com/hjxh/ 2>/dev/null|grep -A1 '>Au99.99'|tail -1").read().split('<td>')[1].split('<')[0]

gpdb  = sophia()
waittime = 1200
def InsertGold():
    gpdb.name = '黄金价格'
    gpdb.date = time.strftime('%Y-%m-%d %H:%M:%S')
    gpdb.value = GetGoldPrice.gold_price
    gpdb.save()

def DeleteGold():
    T = sophia.delete().where(sophia.id == 2)
    T.execute()

def UpdateGold():
    T = sophia.update(value = '666').where(sophia.id == 4)
    T.execute()

    T = sophia.get(id = 3)
    T.value = '999'
    T.save()

def CheckGold():
    #T_list = sophia.select().where(sophia.value == 269.57).order_by(sophia.value).limit(1)
    T_list = sophia.select().order_by(sophia.date.desc()).limit(1)
    for T in T_list:
       # print(T.name.encode,T.value,T.date)
        global gv,gvtime
        gv = T.value
        gvtime = T.date
        #print(gv)
 #   T = sophia.get()#
 #   print(T.id,T.value,T.date,T.name)


def Main_choice(Num):
    if Num == 0:
        InsertGold()
    elif Num == 1:
        DeleteGold()
    elif Num == 2:
        UpdateGold()
    elif Num == 3:
        CheckGold()
    else:
        print('Sorry, error enter.')
def main(i,Num):
    if i == 1:
        Main_choice(Num)
    elif i == 2:
        while True:
            Main_choice(Num)
            time.sleep(waittime)

def repotGoldStatus(lastGoldPrice,newGoldPrice,lastTime,newTime):
    firstNu=14
    secondNU=23
    print('Last gold is:'.ljust(firstNu) + str(lastGoldPrice)).ljust(secondNU) + 'at ' + str(lastTime)
    print('New gold is:'.ljust(firstNu) + str(newGoldPrice)).ljust(secondNU) + 'at ' + str(newTime)
    print('Http gold is:'.ljust(firstNu) + str(httpGoldPrice)).ljust(secondNU) + 'at ' + str(newTime)
def JudgeGold():
    main(1,3)
    lastGoldPrice = gv
    lastTime = gvtime
    main(1,0)
    main(1,3)
    newGoldPrice = gv
    newTime = gvtime
    if lastGoldPrice == newGoldPrice:
        print('Gold price has no change.')
        repotGoldStatus(lastGoldPrice, newGoldPrice, lastTime, newTime)
    elif lastGoldPrice > newGoldPrice:
        print('The price of gold has gone down!')
        repotGoldStatus(lastGoldPrice, newGoldPrice, lastTime, newTime)
    elif lastGoldPrice < newGoldPrice:
        print('The price of gold has gone up!')
        repotGoldStatus(lastGoldPrice, newGoldPrice, lastTime, newTime)

if __name__ == '__main__':
    JudgeGold()