#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
"""
# filter 过滤器函数返回的是迭代器对象，需要通过list()来转换

def is_odd(n):
    return n%2 == 1

templist = filter(is_odd,[1,2,3,4,5,6,7,8,9,10])

print(list(templist))
