#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
生成 1G 个随机数
'''

__author__ = 'Gymgle'
__date__ = '$2014-4-2 14:00:00$'

import random
import time

start = time.clock()
total = 1024*1024*1024
i = 0

try:
    randfile = open('bin.txt', 'w+')
    while i < total:
        randfile.write(str(random.randint(0, 1)))
        i = i + 1
finally:
    randfile.close()

end = time.clock()
print 'Elapsed time: ', end - start, 's'
