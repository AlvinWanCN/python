#!/usr/bin/python
#coding:utf-8
import time
import thread
'''
def loop0():
    print ("start loop0 at:",time.ctime())
    time.sleep(4)
    print("loop0 down at:",time.ctime())


def loop1():
    print ("start loop1 at:",time.ctime())
    time.sleep(2)
    print("loop1 down at:",time.ctime())

def main():
    print("all is start at:",time.ctime())
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    print("all is down at:",time.ctime())

if  __name__ == "__main__":
    main()

'''
def loop(nloop,nsec):
    print("start loop%s at:"%nloop, time.ctime())
    time.sleep(nsec)
    print("loop%s down at:"%nloop, time.ctime())

def main():
    print("all is start at:", time.ctime())
    sleep_list = [4,2,5,7,1]
    for i in range(len(sleep_list)):
        thread.start_new_thread(loop,(i,sleep_list[i]))
    time.sleep(max(sleep_list)+1)
    print("all is down at:", time.ctime())
if __name__ == '__main__':
    main()