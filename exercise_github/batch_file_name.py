#! /usr/bin/python3
# codig:utf-8

"""
批量修改文件名思路:
1. 拿到第一行行参传进来的文件目录下的所有文件名
2. 使用os.path.split(filename)将名字拆成文件名和扩展名存于split_file元祖汇总
split_file[0]为文件名，split_file[1]为扩展名
3. 循环比较文件的扩展名是否需要被替换
4. 如果是，则文件名和扩展名拼接在一起组成新文件名名
5. 执行os.rename()把work_dir\filename,替换成work\newfile
"""
import os
import argparse

def batch_rename(work_dir,old_ext,new_ext):
    #拿到文件目录下的所有文件名
    for filename in os.listdir(work_dir):
        #获取文件扩展名
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        #判断文件的扩展名是否改变
        if old_ext == new_ext:
            new_file=split_file[0]+new_ext
            # 写文件
            os.rename(os.path.join(work_dir,filename),os.path.join(work_dir,new_file))

def get_parser():
    # 生成一个解析处理器，带有描述
    parser = argparse.ArgumentParser(description="change extentsion of files in a working directory ")
    parser.add_argument("work_dir", metavar="WORK_DIR",type=str, nargs=1,help="the directory where to change extension")
    parser.add_argument("old_ext",metavar="OLD_EXT",type=str,nargs=1,help="old extension")
    parser.add_argument("new_ext",metavar="NEW_EXT",type=str,nargs=1,help="new extension")
