#!/usr/bin/env python3

"""
Rename files with the Unix time.
The files are come from Android Wechat folder:
    /Tencent/MicroMsg/WeiXin/
rules:
    1482227010527.mp4 -> 2016-12-20 17.43.30.mp4
    mmexport1482227010527.jpg -> 2016-12-20 17.43.30.jpg

author: Gymgle
date: 2016-12-20
"""

import os
import datetime

if __name__ == "__main__":
    PATH = "."
    LENMP4 = len("1482227010527.mp4")
    LENJPG = len("mmexport1482227010527.jpg")

    for filename in os.listdir(PATH):
        if len(filename) == LENMP4 or len(filename) == LENJPG:
            if filename.startswith("mmexport"):
                timestamp = filename[len("mmexport"):-4]
                newName = datetime.datetime.fromtimestamp(int(timestamp)/1e3).strftime("%Y-%m-%d %H.%M.%S")
                newName += ".jpg"
            else:
                timestamp = filename.split(".")[0]
                newName = datetime.datetime.fromtimestamp(int(timestamp)/1e3).strftime("%Y-%m-%d %H.%M.%S")
                newName += ".mp4"

            try:
                os.rename(filename, newName)
                print(filename + " -> " + newName)
            except OSError as err:
                print("OS Error: {0}{1} already exists.".format(err, newName))
