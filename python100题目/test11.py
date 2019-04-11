#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
"""
# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
'''
        祖  孙  曾1 曾2 曾3...
n=1     1
n=2     1
n=3     1   1
n=4     1   1   1
n=5     1   1   1   2
n=6     1   1   1   2   3
.....
所以是斐波那切数列
'''
# 使用递归
# 1.极限条件  n=1 or n=2 return 1
# 2.fib(n-1)+fib(n-2)
'''
def Fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(5))  # 第20个月出生的兔子数量
'''

# 使用数组结构编写
ls = []
def Fibonacci(n):
    if n==1 :
        ls = [1]
    elif n==2:
        ls = [1,1]
    else:
        ls = [1,1]
        for i in range(2,n):
            # ls[i] = ls[i-1]+ls[i-2]  # 不能这么写的缘故是因为列表添加不能使用这种方法进行添加
            last = ls[i-1]+ls[i-2]
            ls.append(last)
    return ls


print(Fibonacci(20))

