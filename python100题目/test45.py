#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月24日 20:34 
tip-->兴趣是最好的老师<--
"""
# 统计 1 到 100 之和。
# 传统思路
'''
def eqldifSum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
print(eqldifSum(100))
'''
# 变通的思路
def eqldifSum(n):
    sum = 0
    consult = n//2   #商
    remainder = n%2
    if remainder == 0:
        sum = (1+n)*consult
    else:
        sum = (1+n)*consult+consult+1
    return sum

# 等差数列求和公式  sum =n*a1 + n(n-1)/2*d




print(eqldifSum(101))