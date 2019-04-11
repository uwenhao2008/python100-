#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月22日 13:52 
tip-->兴趣是最好的老师<--
"""
# 有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
# 问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
# 使用递归的方式来解决

''''''
from sys import stdout
def recurisionBirth(n):
    if n==1:
        year = 10
        stdout.write(str(year))
    else:
        year = recurisionBirth(n-1)+2
        stdout.write(str(year))
    print()
    # 我之所以经常把这里的return位置弄混，是因为这里return返回的是recurisionBirth()，而这个函数是被递归调用的
    return year

recurisionBirth(5)


'''
# 堆栈堆栈，递归的关键所在为return的位置！！！
def age(n):
    if n == 1:
        c = 10
    else: 
        c = age(n - 1) + 2
    return c
print(age(5))
'''
