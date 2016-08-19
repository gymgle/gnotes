#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
bin.txt 中是 0/1 字符串, 把 Byte 转换为 bit 表示
即: 转换 bin.txt 中每 8 字节 0/1 字符串为 1 字节
例:
    转换前: 01010101 (8字节字符串)
    转换后: 01010101 (用1字节存储)
'''

__author__ = 'Gymgle'
__date__ = '$2014-4-1 12:30:00$'

import struct

hfile = open('bin.txt') # Hex file
bfile = open('bin', 'wb+')   # Bin file

try:
    while True:
        bytenum = hfile.read(8)  # 读取8字节0与1
        if not bytenum:
            break
        tmp = 0
        i = 0
        while i < 8:
            tmp = (tmp << 1) | int(bytenum[i])
            i = i + 1
        bfile.write(struct.pack('B', tmp)) # 写入1字节

finally:
    hfile.close()
    bfile.close()
