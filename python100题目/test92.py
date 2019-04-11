#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月10日 09:48 
tip-->兴趣是最好的老师<--
"""
# 时间函数
if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(30):
        print(i)
    end = time.time()
    # 计算for的执行时间
    print(time.time())
    print(time.clock())    # cpu执行时间
    print(end - start)