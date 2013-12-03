#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

if __name__ == '__main__':
    basename = "/dev/ttyUSB"
    for i in range(10):
        filename = basename+str(i)
        #print filename
        if os.path.exists(filename):
            print filename
            os.popen("sudo killall gpsd")
            os.popen("sudo gpsd "+filename+" -F /var/run/gpsd.sock")
            print "重启gps服务成功。"
            sys.exit(0)
    print "你确定插好了gps模块？gps模块的灯亮了吗？？"
    
        
    

			
