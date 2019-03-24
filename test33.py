#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月23日 00:11 
tip-->兴趣是最好的老师<--
"""
# 按逗号分隔列表。
ls = ['a','b','c','d','e','f']
# lst = ','.join(ls)
lst = ','.join(str(i) for i in ls)
print(lst)