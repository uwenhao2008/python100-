#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
"""
# 判断101-200之间有多少个素数，并输出所有素数
# 学习心得，熟练掌握 continue 和 break
def primeNum(n,m):
    ls = []
    for i in range(n,m+1):
        count = 0
        for j in range(2,i):
            # count=0  if i%j==0 else 1   #这里需要break的，所以不能使用三元
            if i%j == 0:
                count = 1
                # continue   # 继续下一次循环，没有跳出当前循环体
                break        # 跳出当前循环体
        if count == 0:
            ls.append(i) 
                # print("{}不是质数，可以被{}整除".format(i,j))
    print("质数序列为：",ls)

primeNum(101,200)