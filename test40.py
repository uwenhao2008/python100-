#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月24日 14:00 
tip-->兴趣是最好的老师<--
"""
# 将一个数组逆序输出。
ls = ['a','b','c','d','e','f','g']
# 方法一：高级语法
# print(ls[::-1])

# 方法二：采用列表序号的方式
templs =[]
for i in range(len(ls)):
    templs.append(ls[len(ls)-1-i])
print(templs)