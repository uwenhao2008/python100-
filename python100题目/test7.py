#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
"""
# 将一个列表的数据复制到另一个列表中。
lst1 = [2,3,4,55,74]
# b = lst1    #  这里没有进行复制，只是做了一个内存地址的指针！！
b = lst1[:]
print(id(lst1),id(b))