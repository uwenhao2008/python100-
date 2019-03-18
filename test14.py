#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
"""
# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
ls =[]
def disPrime(n):
    for i in range(2,n):
        # 余数，除数
        rem,div = n%i,n//i
        if rem == 0:
            disPrime(div)
        else:
            ls.append(div)
    return ls
print(disPrime(90))
