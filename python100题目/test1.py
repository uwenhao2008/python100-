#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
"""
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 我的代码心得，先找问题的共性，不要一上来的就开始写代码
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=k) and (i!=j) and (j!=k):
                print(i,j,k)