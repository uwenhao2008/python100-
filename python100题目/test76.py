#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月01日 18:20 
tip-->兴趣是最好的老师<--
"""
# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
rawData = int(input("请输入参数n"))
def modiList(r):
    ls = []
    if r%2 == 0:
        times = r//2
        for i in range(1,times+1):
            ls.append(round(1/(2*i),2))
        return ls
    else:
        times = (r+1)//2
        for i in range(1,times+1):
            ls.append(round(1/(2*i-1),2))
        return ls

def sumList(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return sum

if __name__ == '__main__':
    l = modiList(rawData)
    print(l)
    s = sumList(l)
    print("和s为{}".format(s))