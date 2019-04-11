#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
"""
# 暂停一秒输出，并格式化当前时间。
import time
def sleepForOne():
    ti = time.localtime()
    print("当前时间为{}年{}月{}日，{}时{}分{}秒,系统开始睡觉10秒".format(ti[0],ti[1],ti[2],ti[3],ti[4],ti[5],ti[6]))
    time.sleep(10)
    ti = time.localtime()
    print("当前时间为{}年{}月{}日，{}时{}分{}秒".format(ti[0],ti[1],ti[2],ti[3],ti[4],ti[5],ti[6]))

sleepForOne()
