#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月09日 20:00 
tip-->兴趣是最好的老师<--
"""
# 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
# 每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
# n1,n2,n3,n4分别代表  千 百 十 个位
def hashcode(n):
    ls = []
    if n//1000 >= 1:
        ls.append(n//1000)  #千位
        ls.append(n%1000 // 100)  #百位
        ls.append(n%100 //10)   #十位数
        ls.append(n%10)   #个位数
        print(ls)
        ls = [x+5 for x in ls]
        print(ls)
        ls = [x%10 for x in ls]
        print(ls)
        ls[0],ls[-1] = ls[-1],ls[0]
        ls[1],ls[2] = ls[2],ls[1]
        print(ls)
    else:
        print("加密的数据无效")

hashcode(8988)

# 编写 encode和 decode 函数