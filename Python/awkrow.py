#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
实现类似awk取某一列的功能，分隔符这里使用的是#
'''

__author__ = 'Gymgle'
__date__ = '$2014-3-13 13:00:00$'

sfile = open('multirow.txt');
dfile = open('onerow.txt', 'w+')

try:
    while True:
        line = sfile.readline()
        if not line:
            break
        # 每行使用分隔符'#'隔开后，把第二列写入dfile文件
        strlist = line.split(" # ")
        dfile.write(strlist[1] + '\n')
finally:
    sfile.close()
    dfile.close()
