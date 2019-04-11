#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月24日 20:26 
tip-->兴趣是最好的老师<--
"""
# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
x = [[4,3,3],
     [2,8,6],
     [7,7,9]]
y = [[3,8,5],
     [6,9,1],
     [2,8,6]]

s = []
for i in range(3):
    s.append([])
    for j in range(3):
        s[i].append(x[i][j]+y[i][j])
print(s)