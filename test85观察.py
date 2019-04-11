#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月09日 10:33 
tip-->兴趣是最好的老师<--
"""
# 输入一个奇数，然后判断最少几个 9 除于该数的结果为整数
rawData = int(input("请输入一个奇数"))
def divisionX():
    n = '9'
    while 1:
        if int(n)%rawData == 0:
            print(int(n))
            print("{}可以整除{}".format(n,rawData))
            break
        else:
            n += '9'
    else:
        print("XXXX---XXXX")

divisionX()


