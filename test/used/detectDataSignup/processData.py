#!/usr/bin/python
from fdb import useDB as udb1
from tdb import useDB as udb2

fudb=udb1()
tudb=udb2()

tudb.queryDB('select createDate from SignUp')

