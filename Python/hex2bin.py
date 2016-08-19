#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 把十六进制字符串转换为二进制形式, 两字节变1字节
# 例: 源文件内容:    FFEE...       (字符串形式)
#     转换后文件内容 \xFF\xEE\x... (二进制形式)
#
# 又例：源文件内容:    30314142... (字符串形式)
#       转换后文件内容 01AB...     (字符串形式)
# Update: 2016-08-19

__author__ = 'Gymgle'
__date__ = '$2014-4-2 10:00:00$'

import time
import struct

start = time.clock()

sfile = open('hex.txt')			# Hex file
dfile = open('bin', 'wb+')		# Bin file

try:
    while True:
        hexnum = sfile.read(2)  # 读取2个十六进制字符
        if not hexnum:
            break
        dfile.write(struct.pack('B', int(hexnum, 16))) # 以二进制写入
finally:
    sfile.close()
    dfile.close()

end = time.clock()
print('Elapsed time: ', end-start, 's')
