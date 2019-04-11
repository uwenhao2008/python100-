#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月22日 15:05 
tip-->兴趣是最好的老师<--
"""
# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
rawInput = input('请输入5位以内的整数')
length = len(rawInput)
if length<=5:
    print('输入的数字是{}位数'.format(length))
    # ls = list(rawInput).reverse()   # 这里之所以用这种方式得到的是None，因为list()有返回值，返回的是列表，
    # 而list.reverse()没有返回值，只是改变了列表本身   我如果连用的话，相当于在还没有返回的情况下我进行了reverse，所以得到的None
    ls = list(rawInput)
    ls.reverse()
    print(''.join(ls))
else:
    print('数据非法')