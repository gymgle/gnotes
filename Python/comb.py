#!/usr/bin/env python3
# code: utf-8

# 合并 Random_x.bin 等 1000 个文件为一个
# 其中 x 从 0 到 999

__author__ = 'Gymgle'
__date__ = '$2016-8-16 20:00:00$'

import os

counts = 1000
dst_file = open("bin", "wb+")

for i in range(counts):
    src_file = "rand_" + str(i) + ".bin"
    if os.path.exists(src_file):
        with open(src_file, "rb") as f:
            print(src_file)
            dst_file.write(f.read())
            f.close()

dst_file.close()
print("Combination done.")
