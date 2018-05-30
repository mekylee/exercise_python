#! /usr/bin/python3
# coding:utf-8

"""
__name__:当前的模块名
__main__:模块直接运行时，模块的名称
__name__=='__main__':当模块被直接运行时，以下的代码将被执行；如果模块是被引用时，以下的代码将不被执行
"""

def func():
    print("func in one.py")

print("top_level in one.py")

if __name__=='__main__':
    print("one.py is  running")
else:
    print("one.py is imported into other module")

"""
运行one.py输出结果为：
top_level in one.py
one.py is running
"""