#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月18日 22:01 
tip-->兴趣是最好的老师<--
"""
# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
rawInput = int(input('请输入成绩'))
if rawInput>= 90:
    print("成绩A")
elif 60<=rawInput<=89:
    print("成绩B")
else:
    print("成绩C")