# -*- coding: utf-8 -*-

import os
import subprocess


def pic2webp(path):
    """
    指定目录中的图片文件转成 webp 格式，跳过已经存在对应 webp 格式的图片
    前提条件：mac 中安装 cwebp: brew install webp
    """
    files = list()  # 全部非 webp 的文件
    converted = set()  # 已经转换过的文件名
    for file_name in os.listdir(path):
        pic_name = '.'.join(file_name.split('.')[:-1])
        pic_ext = file_name.split('.')[-1].lower()
        if pic_ext not in ['png', 'jpg', 'jpeg', 'bmp', 'svg', 'webp']:
            continue

        if pic_ext == 'webp':  # 记录已经转换过的文件名
            converted.add(pic_name)
        else:
            files.append(file_name)

    for f in files:
        pic_name = '.'.join(f.split('.')[:-1])
        if pic_name in converted:  # 已经有对应的 webp 文件无需转换
            continue
        cmd = 'cwebp -q 80 "{}/{}" -o "{}/{}.webp"'.format(path, f, path, pic_name)
        subprocess.call(cmd, shell=True)
        print('{}.webp'.format(pic_name))

    return True


if __name__ == '__main__':
    pic2webp('path/to/your/pictures')
