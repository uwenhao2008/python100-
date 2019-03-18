#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月18日 22:12 
tip-->兴趣是最好的老师<--
"""
# 输出指定格式的日期。

import datetime
# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
print(datetime.date.today().strftime('%d/%m/%y'))
# 创建日期对象
myBirthday = datetime.date(1986,6,2)
print(myBirthday)
# 日期算术运算

# 日期替换
