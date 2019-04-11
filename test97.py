#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月10日 11:20 
tip-->兴趣是最好的老师<--
"""
# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止

'''
from sys import stdout
filename = input("输入文件名")
# encoding指定utf-8，否则中文乱码   mode='a'表示直接追加到末尾
fp = open(filename,'a+',encoding='utf-8')
ch = input("请输入文件内容")
while ch != '#':
    fp.write(ch)
    # 手动换行
    fp.write('\n')
    stdout.write(ch)
    ch = input("请输入文件内容")
fp.close()
'''

# 'gbk' codec can't decode byte 0xad in position 21: illegal multibyte sequence
# 解决方法1
fname = open('tsfile.txt','rb')
# 解决方法2
fname = open('tsfile.txt','r',encoding='utf-8')
def readfile(fname):
    # str1 = fname.read()
    ls = []
    for i in range(5):
        str1 = fname.readline()
        ls.append(str1)
    # print(ls)
        p = str1
        # print(p)
        if p == 'bei\n':   #因为换行符的缘故，导致我找不到文本里的bei字符串，所以得添加 \n才可以
            print('YYY')
        else:
            print("XXX")
readfile(fname)

    