#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月26日 09:25 
tip-->兴趣是最好的老师<--
"""
# 写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
# 我这里试一试 __str__这个类里的方法
class calculateStrLen:
    def __init__(self,sInput):
        self.sInput = sInput
    def __str__(self):
        return '这是一个奇葩的结果,得到的结果是%s'%self.sInput

if __name__ == '__main__':
    cl = calculateStrLen(input("请输入字符串"))
    print(cl)