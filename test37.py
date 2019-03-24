#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月23日 22:15 
tip-->兴趣是最好的老师<--
"""
# 对10个数进行排序。  采用冒泡排序的方法
# 还可以考虑使用while来实现
ls = [33,45,22,1,67,3,11,33,89,1]
def bubbleSort(l):
    if isinstance(l,list):
        for i in range(len(l)):
            for idx in range(len(l)-i-1):
                if ls[idx]>ls[idx+1]:
                    ls[idx],ls[idx+1] = ls[idx+1],ls[idx]
        return ls
    else:
        print('参数不对')

print(bubbleSort(ls))