#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年11月15日 10:07 
tip-->兴趣是最好的老师<--
# 记录一些有意思的写法
"""
a = [x for x in range(1,101)]
b = [a[x:x+3] for x in range(0,len(a),3)]
print(b)