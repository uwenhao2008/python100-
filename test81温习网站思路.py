#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月07日 14:53 
tip-->兴趣是最好的老师<--
"""
# 809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。
# 求??代表的两位数，及809*??后的结果。
# 心得，这里通过i<100来划分几位数，我脑子里的第一个设想是通过列表，然后len()，哎~~~~ 
# 好好研究网页的其他解决思路

num = 809
for i in range(10,100):
    mul = num*i
    if mul>=1000 and 8*i<100 and 9*i>=100:
        print("{0} * {1} = 800 * {1} + 9 * {1}".format(num,i))


'''
# 下面的思路非常好，但是我不太理解
l1=[m for m in range(10,int(100/8+1))]
l2=[m for m in range(12,int(1000/9+1))]
for i in l1:
    if i in l2:
        k=i
print(l1,l2,k)
'''