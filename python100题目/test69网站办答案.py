#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月25日 23:22 
tip-->兴趣是最好的老师<--
http://www.runoob.com/python/python-exercise-example69.html
"""
if __name__ == '__main__':
    nmax = 50
    n = int(input('请输入总人数:'))
    num = []
    for i in range(n):
        num.append(i + 1)
 
    i = 0
    k = 0
    m = 0
 
    while m < n - 1:
        if num[i] != 0 : k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 1
        i += 1
        if i == n : i = 0
 
    i = 0
    while num[i] == 0: i += 1
    print(num[i])