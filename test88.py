#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月09日 19:31 
tip-->兴趣是最好的老师<--
"""
# 读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊
n = 0
while n<=7:
    rawData = int(input("请输入1~50内的整数"))
    star = ''
    for i in range(rawData):
         star += '*'
        #  这里其实可以通过    rawData * '*'来实现
    print(star)
    n += 1