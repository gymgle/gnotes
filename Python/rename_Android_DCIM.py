#!/usr/bin/env python3

"""
This script customs the file name as:
    Raw file name: IMG_20161201_071251.jpg
    to
    New file name: 2016-12-01 07.12.51.jpg

author: Gymgle
data: 2016.12.15
"""

import os


def custom_filename(filename):
    """Custom file name to IMG, VID and PANO
    Some special file name may be:
    IMG_20161201_071251_1.jpg
    IMG_20161201_071251_HHT.jpg
    """
    names = filename.split("_", 2)
    name_date = names[1]
    name_left = names[2]
    new_name = name_date[:4] + "-" + name_date[4:6] + "-" + name_date[6:]
    new_name += " "
    new_name = new_name + name_left[:2] + "." + name_left[2:4] + "." + name_left[4:]
    return new_name

if __name__ == "__main__":
    FILE_PATH = "."
    for filename in os.listdir(FILE_PATH):
        if (filename.find("IMG_") != -1) or (filename.find("VID_") != -1) or (filename.find("PANO_") != -1):
            new_name = custom_filename(filename)
            try:
                os.rename(filename, new_name)
                print(filename + " -> " + new_name)
            except OSError as err:
                print("OS Error: {0}{1} already exists.".format(err, new_name))
