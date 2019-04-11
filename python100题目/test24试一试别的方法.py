#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月22日 10:39 
tip-->兴趣是最好的老师<--
"""
# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""
------------------------------------------------------
思路：分子，分母可以看做是错位的斐波那契额数列
可以试一试纯数列解决的方法
------------------------------------------------------
"""
def Fibonacci(n):
    if isinstance(n,int):
        if n==1:
            ls = [1]
            return ls
        elif n==2:
            ls = [1,2]
            return ls
        else:
            ls = [1,2]
            [ls.append(ls[-1]+ls[-2]) for i in ls if len(ls)<21]
            return ls
    else:
        print('参数n不对')


def mulSum():
    sum = 0
    ls = Fibonacci(20)
    for i in range(20):
        sum += ls[i+1]/ls[i]
    return sum
print(mulSum())