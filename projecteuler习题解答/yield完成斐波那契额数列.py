#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年11月06日 16:32 
tip-->兴趣是最好的老师<--
使用迭代器完成斐波那契额数列
好处：
1.逻辑清晰
2.内存占用少，因为我以前用序列的那种方式会导致序列很长的时候，占用很大的内存
3.https://www.runoob.com/w3cnote/python-yield-used-analysis.html  清单1里使用print，导致函数复用性差，因为fab没有返回值，若是使用list保存，又会导致问题2占用内存
4.每次调用 fab 函数都会生成一个新的 generator 实例，各实例互不影响  
5.f.read读取文件，可以设置缓冲区，合理利用内存
"""
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1

for i in fab(20):
    print(i)
