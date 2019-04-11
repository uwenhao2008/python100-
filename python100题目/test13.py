#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
"""
# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
import math
def narcisNumber(n):
    ls = []
    # if len(str(n)) != 3:
    #     print("必须输入大于等于100的参数三位数")
    #     return 
    for i in range(100,n):
        if math.pow(int(str(i)[0]),3)+math.pow(int(str(i)[1]),3)+math.pow(int(str(i)[2]),3) == i:
            ls.append(i)
    print(ls)

narcisNumber(1000)

'''
# 我自己的脑回路太奇特了~~~
for n in range(100,1000):
    i = n / 100
    j = n / 10 % 10
    k = n % 10
    if n == i ** 3 + j ** 3 + k ** 3:
        print n
'''