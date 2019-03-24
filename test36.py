#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月23日 00:32 
tip-->兴趣是最好的老师<--
"""
# 求100之内的素数。
def sumPrimenum(n):
    ls = []
    for i in range(1,n+1):
        count = 1   #质数的标志位
        if i==1 or i==2 or i==3:
            ls.append(i)
        else: 
            for j in range(2,i):
                if i%j==0:
                    count += 1
                    break
            # 我之所以这里逻辑混乱，就是因为if判断循环嵌套的位置弄错了
            if count == 1:
                ls.append(i)
    return ls
    
print(sumPrimenum(100))