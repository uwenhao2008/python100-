#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月18日 23:20 
tip-->兴趣是最好的老师<--
"""
# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
# rawInput = input("请输入需要进行叠加的基数与位数，用,间隔")
import math
rawInput = '2,4'
ls = [int(rawInput[0]),int(rawInput[-1])]

for idx in range(ls[1]):
    
