#!/usr/bin/python
from sophdb import test_table



def checkGold():
    t_list = test_table.select().where(test_table.id == 1 )
    for T in t_list:
        print(T.id,T.name)

checkGold()