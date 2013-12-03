#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from gps import *
from time import *
import time
import threading
#import socket

gpsd = None #seting the global variable

os.system('clear') #clear the terminal (optional)

class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd #bring it in scope
        gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
        self.current_value = None
        self.running = True #setting the thread running to true

    def run(self):
        global gpsd
        while gpsp.running:
            gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

if __name__ == '__main__':
    gpsp = GpsPoller() # create the thread

    if len(sys.argv)==2:
        filename = sys.argv[1]+'.txt'
        if  os.path.isfile(filename):
            print filename+" 已经存在。 删除这个文件或者选择另外一个文件名。"
            sys.exit()
        file  = open(filename,'a')
    else:
        print "请指定一个文件名,根据测试情况设置，如 1.1.1 , 则生成1.1.1.txt"
        sys.exit(0)
    cnt = 0
    try:
        gpsp.start() # start it up
        cnt = 0
	lastmsg=''
        while True:
            #It may take a second or two to get good data
            #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc

            os.system('clear')
            #msg = '3#' + str('%.3f' % time.time()) +'#'+str(gpsd.fix.latitude) + '#' + str(gpsd.fix.longitude) + '#' + str(gpsd.fix.speed)+'#'
            msg =  str(gpsd.fix.latitude) + '#' + str(gpsd.fix.longitude)
            print msg
            if gpsd.fix.latitude < 30:
                print "invalid value"
                continue
            if str(gpsd.fix.latitude) == 'nan':
                print "invalid value"
                continue
            #s.sendto(msg,address)
            #s.sendto(msg,address2)
            #s.sendto(msg,address2)
            #print
            #print ' GPS reading'
	    if msg != lastmsg:
            	file.write(msg+'\n')
            	cnt = cnt+1
		lastmsg = msg
            if cnt == 10:
                file.close()
		#print filename
                print "保存文件 "+filename+" 成功。 按 Ctrl + Z 关闭程序。"
                sys.exit(0)
            #print '----------------------------------------'
            #print 'latitude    ' , gpsd.fix.latitude
            #print 'longitude   ' , gpsd.fix.longitude
            #print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
            #print 'time utc    ' , gpsd.fix.time
            #print 'altitude (m)' , gpsd.fix.altitude
            #print 'eps         ' , gpsd.fix.eps
            #print 'epx         ' , gpsd.fix.epx
            #print 'epv         ' , gpsd.fix.epv
            #print 'ept         ' , gpsd.fix.ept
            #print 'speed (m/s) ' , gpsd.fix.speed
            #print 'climb       ' , gpsd.fix.climb
            #print 'track       ' , gpsd.fix.track
            #print 'mode        ' , gpsd.fix.mode
            #print
            #print 'sats        ' , gpsd.satellites
            #print  'heading     ' , gpsd.heading

            time.sleep(0.5) #set to whatever

    except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
        print "\nKilling Thread..."
        file.close()
        gpsp.running = False
        gpsp.join() # wait for the thread to finish what it's doing
    
    print "Done.\nExiting."
