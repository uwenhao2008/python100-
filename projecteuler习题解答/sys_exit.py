#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年06月21日 15:17 
tip-->兴趣是最好的老师<--
"""
# sys.exit函数

import sys
def exitfunc(value):
    print("我是exitfunc的参数value：",value)
    # 只有0可以正常推出，其他的都会异常   下面的之所以90不报错，是因为我是用的是try except
    sys.exit(0)

print("进入函数")

try:
    sys.exit(90)
except SystemExit as value:
    exitfunc(value)

print("???")   # 函数结束了，直接不执行 因为前面的sys.exit(0)
