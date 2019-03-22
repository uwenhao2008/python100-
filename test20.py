#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月19日 20:20 
tip-->兴趣是最好的老师<--
"""
# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""
------------------------------------------------------
思路：第一次 100，第二次弹起来+落地距离刚好等于第一次的100，第三次 上+下为第二次的高度 ... 第十次：
------------------------------------------------------
"""
def jumpMeter(high,times):
    ls = []  # 每次反弹的高度   第一次认为是从0弹到100，单独计算
    for idx in range(times):
        if idx == 0:
            ls.append(high)
            print('第1次反弹的高度为：%s米'%ls[idx])
            continue
        high /= 2
        ls.append(round(high,2))
        print('第{}次反弹的高度为:{}米'.format(idx+1,ls[idx]))
    return ls

print(jumpMeter(100,10))    

# 计算第10次落地的时候，共经历了多少米
l = jumpMeter(100,10)
# 第2到10次弹过的长度
long = [item*2 for item in l if item != 100]
# print(long)