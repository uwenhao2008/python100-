#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月25日 22:42 
tip-->兴趣是最好的老师<--
"""
# 对比__str__和__repr__
class D(object):
    def __str__(self):
        return "a __str__"
    def __repr__(self):
        return "a_repr__"
dr = D()
# 命令行 输入下面内容
'''
dr = D()
print(dr)
dr
"%s"%dr
"%r"%dr
'''