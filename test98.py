#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月11日 09:25 
tip-->兴趣是最好的老师<--
"""
# 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
rawInput = input("请输入需要追加的内容")
fname = open('tsfile.txt','a')
while rawInput != '#':
    rawInput = rawInput.upper()
    fname.write(rawInput)
    fname.write('\n')
    rawInput = input("请输入需要追加的内容")
fname.close()