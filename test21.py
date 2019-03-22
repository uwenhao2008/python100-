#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月19日 21:03 
tip-->兴趣是最好的老师<--
"""
# 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
def peachMonkey(left,days):
    perday_peach = []
    for idx in range(days):
        if idx == 0:
            perday_peach.append(1)
            continue
        perday_peach.append((perday_peach[idx-1]+1)*2)
    return perday_peach

print('第一天猴子摘桃子的数量为{}颗'.format(peachMonkey(1,10)[-1]))