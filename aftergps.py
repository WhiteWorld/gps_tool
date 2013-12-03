#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "请输入*一个*文件夹名称。"
	else:
		filename = sys.argv[1]
		if os.path.exists(filename):
			print "文件夹已经存在，请换一个。"
		else:
			os.popen('mkdir '+filename)
			os.popen('mv *.txt '+filename)
			print "所有txt数据保存以保存至 "+filename+" 文件夹，收工！"
			
