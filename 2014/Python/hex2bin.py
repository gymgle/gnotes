#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
hex.txt是十六进制的数字，目的是要转换为二进制表达，以ASCII形式存放到bin.txt中
举例：
    转换前：1A2F
    转换后：0001101000101111
'''

__author__ = 'Gymgle'
__date__ = '$2014-3-26 10:00:00$'

dt = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111'
    }

hfile = open('hex.txt') # Hex file
bfile = open('bin.txt', 'w+')   # Bin file
i = 0

try:
    while True:
        hexnum = hfile.read(1)  # 读取一个十六进制字符
        if not hexnum:
            break
        bfile.write(dt[hexnum]) # 写入二进制
finally:
    hfile.close()
    bfile.close()
