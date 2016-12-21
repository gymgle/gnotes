#!/usr/bin/env python3

"""
Rename Wechat videos in form of "20xx-xx-xx xx.xx.xx.mp4"
The videos are come from Android Wechat folder:
    /Tencent/MicroMsg/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/video/
rules:
    19 15 38 24 11 16 e34a53c87982.mp4 (没有空格且文件名长度不固定)
    %H %M %S %d %m %y
->  2016-11-24 19.15.38.mp4

author: Gymgle
date: 2016-12-21
"""

import os

if __name__ == "__main__":
    PATH = "."

    for filename in os.listdir(PATH):
        if filename.endswith(".mp4") and filename[:-4].isalnum():
            H = filename[0:2]
            M = filename[2:4]
            S = filename[4:6]
            d = filename[6:8]
            m = filename[8:10]
            y = filename[10:12]
            newName = "20" + y + "-" + m + "-" + d + " " + H + "." + M + "." + S + ".mp4"
            print(filename + " -> " + newName)

            try:
                os.rename(filename, newName)
            except OSError as err:
                print("OS Error: {0}".format(err))
