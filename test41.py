#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月24日 14:15 
tip-->兴趣是最好的老师<--
"""
# 模仿静态变量的用法。
def varfunc():
    var = 0
    print('var = %d' % var)
    var += 1

# 这么写的原因是 作为主运行文件被调用的时候，会执行
if __name__ == '__main__':
    for i in range(3):
        varfunc()

# 类的属性
# 作为类的一个属性吧
class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print(self.StaticVar)

# print(Static.StaticVar)
# a = Static()
# for i in range(3):
#     a.varfunc()