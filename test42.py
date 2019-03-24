#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月24日 15:28 
tip-->兴趣是最好的老师<--
"""
# 学习使用auto定义变量的用法。
num = 2
def autofunc():
    num = 1
    print('internal block num = %d' % num)
    num += 1
for i in range(3):
    print('The num = %d' % num)
    num += 1
    autofunc()
