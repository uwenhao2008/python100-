#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年06月21日 21:06 
tip-->兴趣是最好的老师<--
"""
# python2 是通过os.mhnod()来创建文件的，而python3直接通过open()，若是没有文件就自动创建
import sys,os
ls = []
print("当前目录是：" ,os.getcwd())
if os.path.exists('test.txt'):
    f = open('test.txt', 'w')
    print('print write into file', file=f)
    f.close()
else:
    f = open('test.txt', 'w')
    print('nofile print write into file \n line2 babablalal', file=f)
    # f.flush()
    ls.append(f.readline())
    print("ls:",ls)
    f.close()