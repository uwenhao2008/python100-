#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年06月21日 14:13 
tip-->兴趣是最好的老师<--
"""
# python参数解析
import sys
# 不能用argv[1]，因为那只表示的第一项
prtcontent = sys.argv[1]
print("第一项",prtcontent)
prtcontent = sys.argv
print(prtcontent[0])
print(prtcontent)

for i in prtcontent:
    print(i)


# D:\IMOOC\workspace\python编程小练习\Python 练习100实例\projecteuler习题解答> python echo.py ppp
# 输出  ppp