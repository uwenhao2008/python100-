#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月18日 17:14 
tip-->兴趣是最好的老师<--
"""
# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# 先找到最小的质数 1
ls =[]
def disPrime(n):
    if not isinstance(n,int) or n<=0:
        print("请真确输入参数n")
        exit()
    if n in [1]:
        print('{}=1'.format(n))
    # 不要陷入for循环的怪圈
    while n not in [1]:
        for i in range(2,n+1):
            if n%i == 0:
                n //= i
                ls.append(i)
                break
    return ls   
print(disPrime(90))
