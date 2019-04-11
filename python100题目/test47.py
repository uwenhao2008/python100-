#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月24日 20:50 
tip-->兴趣是最好的老师<--
"""
# 两个变量值互换。
# 使用函数调用的方式编程序
def exchange(a,b):
    if isinstance(a,int) and isinstance(b,int):
        a,b = b,a
        return a,b
    else:
        print('参数不要求')

if __name__ == '__main__':
    x,y = exchange(2,4)
    print(x,y)