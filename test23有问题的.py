#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月21日 17:26 
tip-->兴趣是最好的老师<--
"""
# 打印出如下图案（菱形）
# 双 for 第一层控制行  第二层控制列
'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''
# 这里直接用print()打印会出错，好好研究研究
# 理解 stdout中的print
from sys import stdout
for i in range(4):
   for j in range(2-i+1):
      stdout.write(' ')
   for k in range(2*i+1):
      stdout.write('*')
   print()

for i in range(3):
   for j in range((3-i)*2-1):
      stdout.write('*')
   for k in range(i+1):
      stdout.write(' ')
   print()
   # 这里打印错位了，是什么原因？
   