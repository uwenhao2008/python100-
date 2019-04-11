#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月08日 16:35 
tip-->兴趣是最好的老师<--
"""
import re
# s = 'Hello  Python world!'
s = 'HelloPython world!'
match = re.match('Hello[\t]*(.*)world!',s)
# match = re.match('Hello[\t](.*)world!',s)
print(match)
print(match.group(0))
print(match.group(1))
print(match.group(2))