#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 转换多个文件
# 把十六进制字符串转换为二进制形式, 两字节变1字节
# 例: 源文件内容:    FFEE...       (字符串形式)
#     转换后文件内容 \xFF\xEE\x... (二进制形式)
#
# 又例：源文件内容:    30314142... (字符串形式)
#       转换后文件内容 01AB...     (字符串形式)
# Update: 2017-01-09

__author__ = 'Gymgle'
__date__ = '$2014-04-02 10:00:00$'

import time
import struct
import os

start = time.clock()

for i in range(1000):
    src_file = 'Random_' + str(i) + '.bin'
    dst_file = 'rand_' + str(i) + '.bin'
    if os.path.exists('Random_' + str(i) + '.bin'):
        sfile = open(src_file)
        dfile = open(dst_file, 'wb+')
        try:
            while True:
                # 读取2个十六进制字符
                hexnum = sfile.read(2)
                if not hexnum:
                    break
                # 以二进制写入
                dfile.write(struct.pack('B', int(hexnum, 16)))
        finally:
            sfile.close()
            dfile.close()
            print(src_file + ' transformed')

end = time.clock()
print('Elapsed time: ', end-start, 's')
