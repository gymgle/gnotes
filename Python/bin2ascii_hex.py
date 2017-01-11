#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
把二进制的文件转换为十六进制ASCII文件，1字节变换为2字节

例：
    源文件内容：   \x12\34\AB\EF    (4字节)
    转换后文件：    1234abef        (8字节)
'''

__author__ = 'Gymgle'
__date__ = '$2017-01-10 19:00:00$'

import binascii

sfile = open('test.dat', 'rb')
dfile = open('log.txt', 'wb+')

try:
    while True:
        hexstr = sfile.read(1)
        if not hexstr:
            break
        hexnum = binascii.b2a_hex(hexstr)
        dfile.write(hexnum)
finally:
    sfile.close()
    dfile.close()
