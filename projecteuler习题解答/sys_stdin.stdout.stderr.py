#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年06月21日 15:38 
tip-->兴趣是最好的老师<--
"""
# sys.stdin stdout stderr
import sys
import time
print("come in")
# ls = "he hel hell hello world"
ls = ['he', 'hel', 'hell', 'hello', 'world']
for i in ls:
    print(i)
    sys.stdout.flush(i)
    time.sleep(1)
