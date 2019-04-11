#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月24日 20:24 
tip-->兴趣是最好的老师<--
"""
# 模仿静态变量(static)另一案例。
class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print('nNum = %d' % self.nNum)

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print('The num = %d' % nNum)
        inst.inc()