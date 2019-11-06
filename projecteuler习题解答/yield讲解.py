#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年11月06日 12:17 
tip-->兴趣是最好的老师<--
https://www.jianshu.com/p/d09778f4e055
"""
# # yield 可以理解为return，不过它出去了以后 还可以再从相同位置进来
# # 下次迭代时，代码从yield的下一跳语句开始执行。!!!!!
# def yield_test(n):
#     for i in range(n):
#         yield call(i)
#         print('i=',i)
#     # 做一些其他事情
#     print('do something')

# def call(i):
#     print(i,'次的i为:',i)
#     return i*2

# # 使用for循环   这里的i为什么收到了 def call的影响，南到是因为我都是用的同一个参数的缘故吗？我把外面的换位j试一试！
# # 经过测试，发现不是这个问题，想想原因！               其实这里的for循环里的j就代表的是每次yield函数的返回值！！！
# # for i in yield_test(5):
# #     print('i=>>>',i)
# for j in yield_test(5):
#     print('j=>>>',j)




# # 迭代其用法理解例子 
# def g():
#     print('1')
#     x = yield 'hello'
#     print('2=','x=',x)
#     y = 5 + (yield x)
#     print('3','y=',y)

# f = g()
# f.__next__()
# # out: 1

# f.send(5)

# f.__next__()
# # out: 2= x= None






# https://blog.csdn.net/u011318077/article/details/93749143
# 包含yield关键字，就变成了生成器函数
# 调用函数并不会执行语句
import time
def foo():
    print('Starting.....')
    while True:
        # 下面若是不写为 res = yield 4 
        res = yield 4
        print("res:", res)

# 下面调用函数并没有执行，可以先将后面的语句注释掉
# 逐行运行代码观察效果
g = foo()
print("第一次调用执行结果：")
time.sleep(5)
print(g.__next__())
# time.sleep(5)
print("*" * 100)

print("第二次调用执行结果：")
time.sleep(10)
print(next(g))
print("*" * 100)





