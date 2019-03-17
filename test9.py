#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
"""
# 暂停一秒输出。
import time
def sleepOnesec():
    ti = time.localtime(time.time())
    # print("当期时间为：{}:{}:{}".format(ti[3],ti[4],ti[5]))
    print("当期时间为：{}:{}:{}".format(ti.tm_hour,ti.tm_min,ti.tm_sec))
    print("睡5秒以后执行~~~")
    time.sleep(5)
    ti = time.localtime(time.time())
    print("当期时间为：{}:{}:{}".format(ti.tm_hour,ti.tm_min,ti.tm_sec))

sleepOnesec()