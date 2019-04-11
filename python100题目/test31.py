#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月22日 16:43 
tip-->兴趣是最好的老师<--
"""
# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
import re
rawInput = input('请输入星期几:').capitalize()

def weekX(s):
    weekChar = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    ls = []
    # 使用正则
    for item in weekChar:
        if re.match(s,item):   #从头完全匹配
        # if re.match('.o.d',item):     #匹配 o*d
        # if re.match('.*u+[ep]*.d',item):     #匹配 u前至少一个符号，其后面至少一个e或p，然后任意字符 然后d
            ls.append(item)
        else:
            continue
    return ls

print(weekX(rawInput))

