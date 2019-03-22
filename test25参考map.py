#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月22日 11:08 
tip-->兴趣是最好的老师<--
"""
# 求1+2!+3!+...+20!的和。
def factorial(n):
    if isinstance(n,int):
        if n==1:
            return 1
        else:
            s = 1
            for i in range(1,n+1):
                s *= i
            return s
    else:
        print("参数n不对")

s = 0
for i in range(1,21):
    s += factorial(i)
print(s)