#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月07日 15:29 
tip-->兴趣是最好的老师<--
"""
# 输入的八进制转换为十进制
rawInput = input("请输入八进制数")
h = rawInput
l = len(h)
n = 0
for i in range(l):
    n += int(h[i])*pow(8,(l-i-1))
print(n)