#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月25日 09:28 
tip-->兴趣是最好的老师<--
"""
# 学习使用按位取反~。
# (1)先使a右移4位。 
# (2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4) 
# (3)将上面二者进行&运算。
a = 10
print(bin(a))
b = a>>4
print(bin(b))
print(bin(~a))
c = ~(~0<<4)
print(c,bin(c))
