#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月01日 18:46 
tip-->兴趣是最好的老师<--
"""
# 字符串排序
str1 = 'abcde'
str2 = 'efdis'
str3 = 'aadk'

if str1 > str2 : str1,str2 = str2,str1
if str1 > str3 : str1,str3 = str3,str1
if str2 > str3 : str2,str3 = str3,str2

print(str1,str2,str3)