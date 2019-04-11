#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月24日 20:46 
tip-->兴趣是最好的老师<--
"""
# 求输入数字的平方，如果平方运算后小于 50 则退出。
while True:
    rawInput = int(input('请输入一个整数'))
    square = rawInput**2 
    print(square)
    if square<50:
        print('不满足循环条件')
        break