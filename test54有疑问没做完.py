#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月24日 21:35 
tip-->兴趣是最好的老师<--
"""
# 取一个整数a从右端开始的4〜7位。
# 程序分析：可以这样考虑： 
# (1)先使a右移4位。 
# (2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4) 
# (3)将上面二者进行&运算。
a = 9
bin(a)
b = a<<4
c = b>>8
print(bin(c))