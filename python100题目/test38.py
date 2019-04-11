#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月23日 23:32 
tip-->兴趣是最好的老师<--
"""
# 求一个3*3矩阵主对角线元素之和。
'''
ls = [3,5,4,2,6,23,11,65,3]
lst = [[x for x in ls[0:3]],[y for y in ls[3:6]],[z for z in ls[6:9]]]
sum = 0
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if i==j:
            sum += lst[i][j]
print(sum)
'''
# 使用控制台依次输入9个数字，然后实现计算对角线的和  这个思路做一下
sum = 0
ls = []
for i in range(3):
    ls.append([])
    # print(ls[i])
    for j in range(3):
        ls[i].append(int(input('请输入第{}个数'.format((i)*3+j+1)))) 
        if i==j:
            sum += ls[i][j]

print(sum)