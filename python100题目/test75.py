#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月01日 18:17 
tip-->兴趣是最好的老师<--
"""
# 算一道简单的题目
if __name__ == '__main__':
    n = 0
    for i in range(5):
        if i != 1: n += 1
        if i == 3: n += 1
        if i == 4: n += 1
        if i != 4: n += 1
        if n == 3: print(64 + i)