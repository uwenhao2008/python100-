#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月10日 11:00 
tip-->兴趣是最好的老师<--
"""
# 字符串日期转换为易读的日期格式。
from dateutil import parser
dt = parser.parse("Aug 28 2015 12:00AM")
print(dt)