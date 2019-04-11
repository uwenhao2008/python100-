#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月25日 22:59 
tip-->兴趣是最好的老师<--
"""
# global关键词的使用，新手不要使用，而且尽量避免这种使用方式,因为会把数据来源弄乱

x = 50
def func():
    global x
    print('x is', x)
    x = 2
    print('Changed local x to',x)

# x = 50
func()
print('Value of x is',x)
