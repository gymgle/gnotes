#!/bin/bash

# 针对文件名中含有空格的情况, 以换行符分割读取到的每个文件, 这种写法并不等同于 IFS=$'\n'
IFS='
'

# 把目录中所有名为 testA 的文件夹称重命名为 testB
# rename 命令并不能处理好文件名包括空格的情况, 因此这里使用 mv 命令

# for in same as 
# find $PWD -type d | grep "testA" | while read file
for file in `find $PWD -type d | grep "testA"`
do
    newfile=`echo $file | sed 's/testA/testB/'`
    echo $file "->" $newfile
    mv $file $newfile
done
