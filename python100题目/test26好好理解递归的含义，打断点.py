#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月22日 11:19 
tip-->兴趣是最好的老师<--
"""
# 利用递归方法求5!
# fact(n) = n*fact(n-1);n==1 return 1
def factRecru(n):
    sum = 0
    if n==1:
        sum = 1
    else:
        sum = n*factRecru(n-1)
    return sum

print(factRecru(5))