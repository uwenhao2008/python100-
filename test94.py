#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月10日 10:32 
tip-->兴趣是最好的老师<--
"""
# 时间函数举例4,一个猜数游戏，判断一个人反应快慢。
import random
import time
dataMatch = random.randint(1,100)         # 得到1~100以内的随机数
print("作弊数字为-->",dataMatch)
def determineNum():
    while 1:
        rawdata = int(input("请输入100以内的整数"))
        if rawdata > dataMatch:
            print("大了")
        elif rawdata < dataMatch:
            print("小了")
        else:
            break

if __name__ == '__main__':
    time_start = time.time()
    determineNum()
    time_end = time.time()
    ti = (time_end - time_start)
    print(ti)
