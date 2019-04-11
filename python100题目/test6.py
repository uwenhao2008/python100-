#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
"""
# 斐波那契数列
def Fibonacci():
    fib = [1,1]
    while len(fib)<= 20:    
        last = fib[-1]+fib[-2]
        if last <= 1200:
            fib.append(last)
            print(fib)
        else:
            break
        

Fibonacci()

# 使用递归
def Fib(n):
    if n==1 or n==2:
        return 1
    return Fib(n-1)+Fib(n-2)
print(Fib(15))