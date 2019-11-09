#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年11月09日 11:58 
tip-->兴趣是最好的老师<--
"""
import sys as sys
# for i in range(250):
#     print(sys.getsizeof(i))
msg = 'this is Your DREA'
print(sys.getsizeof(msg))
print(sys.getsizeof("this is Your DREA"))
print(msg.encode())
msgnew = msg.encode()
print(sys.getsizeof(msgnew))
