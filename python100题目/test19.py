#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月19日 10:29 
tip-->兴趣是最好的老师<--
"""
# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
"""
------------------------------------------------------
思路：对于 n，找出2至n-1间的所有除数，然后判断 n是否等于 他们之和
这里有个函数优化的过程  直接for n//2就可以了，不需要完全循环，回家试一试~~~~
------------------------------------------------------
"""
def sumList(lst):
    sum = 0
    for index in range(len(lst)):
        sum += lst[index]
    return sum

def divisor(n):
    dList = []
    for index in range(1,n//2+1):
        if n%index == 0:
            dList.append(index)
    return dList
# print(divisor(89))

def factorization(n):
    if n == 1:
        print("参数必须大于1")
    ls = []
    for i in range(2,n):
        s = divisor(i)
        if i == 35000:
            print('闪现时间:,20:51:59')
        if i == sumList(s):
            ls.append(i)
            #  '+'.join(string)   还有就是for的妙用  for else的妙用，掌握
            print("完数{}={}".format(i,'+'.join(str(i) for i in s)))
        else:
            continue
    return 

# 我的代码性能有点低，100000以后计算就很慢了
# 不一定要累加，直接累减  最后为0 来判断完数
# 难怪，因为完数本来就少   
factorization(50000000)

