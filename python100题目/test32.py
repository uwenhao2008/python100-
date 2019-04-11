#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月22日 21:06 
tip-->兴趣是最好的老师<--
"""
# 按相反的顺序输出列表的值。
a = ['one','two','three']
for item in a[::-1]:
    l = list(item)
    l.reverse()
    l = ''.join(l)
    print(l,end=' ')
    