#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月09日 12:44 
tip-->兴趣是最好的老师<--
"""
# 回答结果（结构体变量传递）。
class Student:
    x = 0
    c = 0

def f(stu):
    stu.x = 20
    stu.c = 'c'

a = Student()
print(a.x,a.c)
a.x = 3
a.c = 'a'
f(a)
print(a.x,a.c)