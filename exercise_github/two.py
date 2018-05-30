#! /usr/bin/python3
# coding:utf-8

import one

print("top_level in two.py")
one.func()

if __name__=='__main__':
    print("two.py is running")
else:
    print("two.py is imported into other module")

"""
运行two.py输出结果为：
top_level in one.py
one.py is imported into other module
top_level in two.py
func in one.py
two.py is running

"""