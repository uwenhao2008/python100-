#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
"""
# 输出 9*9 乘法口诀表
def multipleTbale(n):
    for i in range(1,n+1):
        ls = []
        for j in range(i,n+1):
            str = '{}*{}={}'.format(i,j,i*j)
            ls.append(str)
            # print(ls)
        print(ls)
multipleTbale(9)