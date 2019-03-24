#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月22日 15:52 
tip-->兴趣是最好的老师<--
"""
# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""
------------------------------------------------------
思路：使用数组处理非常简单，直接ls[1]?ls[-1]之间判断就可以，不过我想换个思路试一试
------------------------------------------------------
"""
def matchNum(n):
    if n//10000 >=1:
        print('位数对的')
        
    else:
        return

# 获取每个进位上的数
# 12345  经过处理后返回[5,4,3,2,1]
def getCarry(m):
    if m//10000 >=1:
        print('位数对的')
        ls = []
        while m>0:  
            step = m%10  #计算位数
            ls.append(step)
            m //= 10
        if ls[0]==ls[-1] and ls[1]==ls[-2]:
            print('输入的数据时回文数')
        else:
            print('NoNoNo')
    else:
        print('参数不满足要求')
rawInput = int(input('请输入5位数'))
getCarry(rawInput)
