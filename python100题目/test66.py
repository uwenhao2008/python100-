#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月25日 14:17 
tip-->兴趣是最好的老师<--
"""
# 输入3个数a,b,c，按大小顺序输出。
# 并交换顺序
from sys import stdout
def swap(a,b):
    return b,a
if __name__ == '__main__':
    n1 = int(input("请输入第一个数"))
    n2 = int(input("请输入第二个数"))
    n3 = int(input("请输入第三个数"))

    if n1>n2:
        n1,n2 = swap(n1,n2)
        # stdout.write()
    if n1>n3:
        n1,n3 = swap(n1,n3)
    if n2>n3:
        n2,n3 = swap(n2,n3)

    print(n1,n2,n3)

    