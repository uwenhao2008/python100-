#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月22日 11:38 
tip-->兴趣是最好的老师<--
"""
# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
from sys import stdout
ls = []
def recurisionReverse(s):
    if isinstance(s,str):
        if len(s)==0:
            return
        else:
            ls.append(s[-1])
            stdout.write(s[-1])
            recurisionReverse(s[0:-1])
    else:
        print('参数s不对')   
    print() 

recurisionReverse('abcde')   