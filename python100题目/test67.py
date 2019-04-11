#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月25日 14:33 
tip-->兴趣是最好的老师<--
"""
# 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
# 网站的方法没有用到list的max、min方式，是否效率更高？
ls = [25,12,99,43,1,6,0,77]

def findIndex(style,ls):
    # print(type(style))
    if style=='fmax':
        imax = ls.index(max(ls))     
        ls[imax],ls[0] = ls[0],ls[imax]
    elif style=='fmin':
        imin = ls.index(min(ls))
        ls[imin],ls[-1] = ls[-1],ls[imin]
    return ls

if __name__ == '__main__':
    findIndex('fmax',ls)
    findIndex('fmin',ls)
    print(ls)
    