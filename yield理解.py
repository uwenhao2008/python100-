#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
"""
# yield的理解
# https://www.jianshu.com/p/d09778f4e055
# 有yield的函数，就不在简单的是一个函数了，而是生成器，这么做的原因就是 a=[1,2,3,4]即便不是用也会占用内存，而生成器只有使用的时候才会迭代生成
# 我们可以用id检测迭代器，只有迭代的时候才会生成
'''
def addlist(alist):
    for i in alist:
        yield i+1

alist = [1,2,3,4]
print('使用前的id-->',id(addlist))
for x in addlist(alist):
    print('使用中的id-->',id(addlist))
    print(x)
'''

'''
# 包含yield的函数，里面没有立即运行
def h():
    print("To be brave")
    yield 5

h()
'''
ls = yield [1,2,3]
print('第一次迭代之前',id(ls))



