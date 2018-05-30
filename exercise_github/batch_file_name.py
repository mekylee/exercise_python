#! /usr/bin/python3
# codig:utf-8

"""
�����޸��ļ���˼·:
1. �õ���һ���вδ��������ļ�Ŀ¼�µ������ļ���
2. ʹ��os.path.split(filename)�����ֲ���ļ�������չ������split_fileԪ�����
split_file[0]Ϊ�ļ�����split_file[1]Ϊ��չ��
3. ѭ���Ƚ��ļ�����չ���Ƿ���Ҫ���滻
4. ����ǣ����ļ�������չ��ƴ����һ��������ļ�����
5. ִ��os.rename()��work_dir\filename,�滻��work\newfile
"""
import os
import argparse

def batch_rename(work_dir,old_ext,new_ext):
    #�õ��ļ�Ŀ¼�µ������ļ���
    for filename in os.listdir(work_dir):
        #��ȡ�ļ���չ��
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        #�ж��ļ�����չ���Ƿ�ı�
        if old_ext == new_ext:
            new_file=split_file[0]+new_ext
            # д�ļ�
            os.rename(os.path.join(work_dir,filename),os.path.join(work_dir,new_file))

def get_parser():
    # ����һ����������������������
    parser = argparse.ArgumentParser(description="change extentsion of files in a working directory ")
    parser.add_argument("work_dir", metavar="WORK_DIR",type=str, nargs=1,help="the directory where to change extension")
    parser.add_argument("old_ext",metavar="OLD_EXT",type=str,nargs=1,help="old extension")
    parser.add_argument("new_ext",metavar="NEW_EXT",type=str,nargs=1,help="new extension")
