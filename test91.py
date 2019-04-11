#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月10日 09:45 
tip-->兴趣是最好的老师<--
"""
# 时间函数
if __name__ == '__main__':
    import time
    print(time.ctime(time.time()))
    print(time.asctime(time.localtime(time.time())))
    print(time.asctime(time.gmtime(time.time())))