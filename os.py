#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys,os
oldSterr = None
logfile = None

try:
        logfile = open('/tmp/1.txt','w+')
        oldStderr = sys.stderr
        sys.stderr = logfile
        os.system('dialog --inputbox "Please input something text:" 10 40')
finally:
        if logfile:
           logfile.close()
#       if oldStdout:
#          sys.stdout = oldStdout

#print 'Hello World in Screen'
