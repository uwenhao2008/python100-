#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年06月20日 21:53 
tip-->兴趣是最好的老师<--
https://blog.csdn.net/MsStrbig/article/details/79823555
"""
# 交换位置
def swap(a: int, b: int):
    temp = a
    a = b
    b = temp

# 全排列递归算法  k是层数 代表第几个数，m表述数组长度
def perms(ls: list, k: int, m: int):
    m = len(ls)
    k = 0
    if k == m:
        # K==m 表示到达最后一个数，不能再交换，最终的排列的数需要输出；
        for i in range(m):
            