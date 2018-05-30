#! usr/bin/python3
# coding:utf-8

import  os

file_dir="D:\Python\Python-master\Python-master"
for filename in os.listdir(file_dir):
    split_file =os.path.splitext(filename)   #pathon.splitext(filename)返回的是元组，（filename,后缀名）
    print(split_file)
    file_ext=split_file[0]
    print(file_ext)