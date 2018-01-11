#!/usr/bin/python
from sophdb import test_table


fileContent=''
def checkGold():
    t_list = test_table.select().where(test_table.id << (1,2) )
    for T in t_list:
        #print(T.id,T.name)
        fileContent =

checkGold()