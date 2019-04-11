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
rawInput = '2,5'
ls = [int(rawInput[0]),int(rawInput[-1])]

lst = []
for idx in range(ls[1]):
    lst.append(int(ls[0] * math.pow(10,idx)))
# 处理数据 lst [2,20,200,2000,20000]
lst2 = []
sum = 0
for i in range(ls[1]):
    for j in range(i+1):
        sum += lst[j]
        continue
    lst2.append(sum)
    sum = 0 
print(lst2)

# 上面的代码还可以优化，sum不需要每次从头计算，在上次的基础上累计，这个思路试一试

# 题者的思路是，每一次直接进行计算后， append到list里

    
