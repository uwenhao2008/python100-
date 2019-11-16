#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年11月15日 10:07 
tip-->兴趣是最好的老师<--
# 记录一些有意思的写法
"""
# # [1,2,3.....99,100] -> [[1,2,3],[4,5,6],....[98,99,100]]
# a = [x for x in range(1,101)]
# b = [a[x:x+3] for x in range(0,len(a),3)]
# print(b)

# # class中嵌套class  第二个class中的self指代谁呢？第一个还是第二个呢？  我目前猜测应该是第二个
# class OUT():
#     def __init__(self):
#         self.out_a = 'out_a'
#     class INNER():
#         def __init__(self):
#             self.inner_b = 'inner_b'
# out = OUT()
# inner = out.INNER()
# print(out.out_a)   # out_a
# print(inner.inner_b)  # inner_b

# # python 类方法调用 类变量
# class Test():
#     ls = 88
#     # @staticmethod
#     @classmethod
#     def ppt(self,s = ls):
#         return s
# a = Test()
# # print(a.ppt())   #  一定要()，否则函数不执行  
# # print(a.ppt(1,99))   #  加@staticmethod  直接输出 99  说明加上这个装饰器以后，ppt函数里的self都被当作一个参数了，和一个外部函数很类似了
# print(a.ppt)

# https://segmentfault.com/a/1190000004994727

# class A():
#     _info = "hello world"
#     @classmethod
#     def a(arg):
#         print(arg._info)
# # 可直接调用，也可以先实例化再调用
# # A.a()
# # or
# # aaa = A()
# # aaa.a()

# class A():
#     _info = "hello world"
#     @staticmethod
#     def a(arg):
#         print(arg._info)
# A.a(1)

# class c():
#     _num = 0

#     def add(self,num):
#         self._num += num
#         print('->',self._num)
#     def add_c(self,num):
#         c._num += num
#         print('-->',c._num)
#     def get(self):
#         return self._num
#     def get_c(self):
#         return c._num

# c1 = c()
# c2 = c()

# c1.add_c(3)     # c._num = 3
# c2.add_c(2)     # c._num = 3+2
# c1.add(9)       # 9+5
# c2.add(4)       # 5+4
# print(c1.get())#?
# print(c2.get())#?
# print(c1.get_c())#?
# print(c2.get_c())#?
 

# class Pizza(object):
#     @staticmethod   # 第一项不需要写self，而且可以当作一般函数一样使用，同时@staticmethod表明这个def是为 这个类服务的
#     def mix_ingredients(x, y):
#         return x + y
 
#     def cook(self):
#         return self.mix_ingredients(self.cheese, self.vegetables)


# cnt = 100  # 全局变量
# class Test():
#     cnt = 0  # 类变量
#     def add(self):
#         self.cnt += 1
#         print(self.cnt)

#     def glb_val(self):
#         global cnt
#         print(cnt)
# a = Test()
# a.add()
# a.glb_val()

# list写法
# print(list((1,2,3)))
# print(list((range(1,10,3))))
# print(list({'a':3,'b':'5'}))  #   ['a','b']  
# print(list({'a':3,'b':'5'}.items()))  #   [('a',9),('b',5)]  

# ls = [1,2,3,4,5]
# del ls[2]  # 删除 3 
# dictitem = {'a':1,'b':11,'c':99}
# del dictitem['b']   # 删除 'b':11

# ls = list(range(11))
# # import random
# # random.shuffle(ls)   # 打乱列表中ls的元素顺序
# print(zip(ls,[1]*11))   # <zip object at 0x000001E956D29808>
# print(list(zip(ls,[1]*11)))  # [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1)]
# print(enumerate(ls))   # <enumerate object at 0x0000020A4DD945E8>
# print(list(enumerate(ls)))   # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]

# print(list(map(str,range(5))))   # ['0', '1', '2', '3', '4']

# def addv5(v):
#     return v+5
# print(list(map(addv5,range(10))))   # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# ****************************
# def add(x,y):
#     return x+y
# print(list(map(add,range(5),range(5,10))))
# # [5, 7, 9, 11, 13]   相当于是 [0,1,2,3,4]每项与[5,6,7,8,9]对应项相加
# print(list(map(add,range(3),range(5,10))))   # [5, 7, 9]   按照最短的项来确定
# print(list(map(lambda x,y: x+y,range(5),range(6,13))))   # [6, 8, 10, 12, 14]   [0,1,2,3,4]对应项与[6,7,8,9,10,11,12]

# def add(x,y):
#     return x+y
# print([add(x,y) for x,y in zip(range(5),range(5,10))])   # [5, 7, 9, 11, 13]
# print(add(x,y) for x,y in zip(range(5),range(5,10)))   # <generator object <genexpr> at 0x000001E5930527D8>
# print(list(zip(range(5),range(7,10)))) # [(0, 7), (1, 8), (2, 9)]
# # ****************************

# from functools import reduce
# seq = [1,2,3,4,5,6,7,8,9,10,11]
# def add(x,y):
#     return x+y
# print(reduce(add,range(10)))
# print(reduce(lambda x,y: x+y,seq))   # sum  [1,2,3,4,5,6,7,8,9,10,11]   相当于 sum([1,2,3,4,5,6,7,8,9,10,11])

# seq = ['foo','x41','?!','***']
# def func(x:str):
#     return x.isalnum()    # str.isalnum()  如果 str至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
# print(filter(func,seq))   # <filter object at 0x0000017BEFE75208>
# # filter函数返回对应位置为True的
# print(list(filter(func,seq)))   # ['foo', 'x41']
# print([filter(func,seq)])   # [<filter object at 0x0000019F937D3710>]
# # list() 和 []  不等价~~~~~~~~~~~
# print([x for x in seq if x.isalnum()])
# print(list(filter(lambda x: x.isalnum(),seq)))
# print(list(filter(None,[1,2,3,0,0,-1,4,-6,5])))  # If function is None, return the items that are true.
# # [1, 2, 3, -1, 4, -6, 5]   为什么这里的-1，-6也会被返回？  items that are true  怎么理解？

# import random
# x = [random.randint(1,100) for i in range(10)]  # 生成10个[1,100]之内的随机数
# print(x)
# print(list(map(lambda i: i+5 , x)))  # 所有元素同时+5

# # 列表推导式
# [x*x for x in range(10)]
# # 相当于
# ls = []
# for x in range(10):
#     ls.append(x*x)
# # 也等价于
# ls = list(map(lambda x: x*x, range(10)))

# # 列表推导式实现平铺
# vec = [[1,2,3],[4,5,6],[7,8,9]]
# print([num for elem in vec for num in elem])
# # 相当于   弄清楚循环的嵌套关系  for  for的顺序
# result = []
# for elem in vec:
#     for num in elem:
#         result.append(num)
# print(result)

# # 用列表推导式实现矩阵转置
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# rev_matrix = [[row[i] for row in matrix] for i in range(4)]
# print(rev_matrix)
# # 相当于
# result = []
# temp = []
# for i in range(4):
#     for row in matrix:
#         temp.append(row[i])
#     result.append(temp)
#     temp = []
# print(result)

# # **********************************
# # 使用列表推导式生成100以内的所有素数
# from math import sqrt   # sqrt  开方
# print([p for p in range(2,100) if 0 not in [p%d for d in range(2,int(sqrt(p))+1)]])

# aList = [3,5,8,7,9]
# aList[:3] = [1,1,1]
# print(aList)   # 直接进行了替换操作  GOOOOOOD

# # 浅复制 深复制 内存id的关系
# aList = [1,3,7,8]
# bList = aList
# bList[1] = 8
# print(aList)  # [1,8,7,8]
# print(aList == bList)    # True
# print(aList is bList)    # True
# print(id(aList) == id(bList))   # True
# bList = aList[:]   # 深复制
# print(aList == bList)    # True
# print(aList is bList)    # False
# print(id(aList) == id(bList))   # False
# print(id(aList[0]) == id(bList[0]))   # True   不要怀疑，即使是深复制，相同值在内存中仍然只有一份
# bList[1] = 11
# print(aList)   #  [1, 8, 7, 8]
# print(bList)   #  [1, 11, 7, 8]
# # Python采用基于值的内存管理模式，变量中不直接存放值，而是存放值大的引用

# ls = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # ls = [range(10)]  # [range(0, 10)]
# # ls = [i for i in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(ls[::2])   #  [0, 2, 4, 6, 8]
# # ls[::2] = [3,5]   # 报错，一位内长度不同
# ls[::2] = [1,1,1,1,1]
# print(ls)
# del ls[::2]
# print(ls)   # [1, 3, 5, 7, 9]

# # 元组 不可变，可作为常量列表  但是元组中包括可变列表的话，情况就复杂了
# x = (3,)    # 元组中只有一个数据的时候，必须加,
# x = ([1,2],2,3)
# x[0][0] = 66
# print(x)   # ([66, 2], 2, 3)   元组中的数组
# # 但是试图直接改变元组值，会报错

# 字典     python内置函数len(),max(),min(),sum(),sorted(),in也可作用域字典，但是默认作用域字典key，
# 若是想作用于元素，即键值对，需要使用字典的items()方法明确指定，若是想作用域值，则需要使用values()明确指定

# # 案例精选 ------------------
# import string
# import random
# x = string.ascii_letters+string.digits+string.punctuation
# print(x)
# y = [random.choice(x) for i in range(1000)]   # 随机在x中选择1000次
# print('->',y)
# z = ''.join(y)
# d = dict()
# for ch in z:
#     # 依次遍历每个字符，若是字典里没有出现过，就设置d[ch]默认值为0 ，若是出现过 就+1
#     d[ch] = d.get(ch,0)+1

# 内置函数 globals()  locals()分别返回当前作用域内所有的全局变量 和 局部变量

# 有序字典  collections.OrderDict()

# x = ['A','B','C','D']
# y = ['a','b','c','d']
# dic = {i:j for i,j in zip(x,y)}
# print(dic)

# 集合 {3,5} 无序可变序列
# 元组 (3,5) 不可变



# list,set,dict速度对比
# import random
# import time
# x = list(range(10000))
# y = set(range(10000))
# z = dict(zip(range(10000),range(10000)))
# r = random.randint(0,9999)

# # start = time.time()
# # for i in range(9999999):
# #     r in x
# # print('time used:',time.time()-start)

# start = time.time()
# for i in range(9999):
#     r in y
# print('time used:',time.time()-start)

# start = time.time()
# for i in range(99999):
#     r in z
# print('time used:',time.time()-start)

# 字典 items() values()
# a = [1,2,3]
# b,c,d = a
# print(c)

# dic = {'a':2,'b':33,'c':56}
# b,c,d = dic.items()
# print(c)  #('b', 33)  键值对
# b,c,d = dic
# print(c)  # 字典默认是处理 键~~~~~~~~~~~~
# b,c,d = dic.values()   # 让变量= 字典 值
# print(c)   

# 计算100以内的最大素数
# 学到了一个很重要的思考方式，以前我是从1循环到100，就会出现 n=1的情况，也会出现range(1,100),代码会变得很长，而且不切题，因为要我找的是<最大>的素数
# Python continue 语句跳出本次循环，而break跳出整个循环(循环嵌套的话跳到上一层了)
# for n in range(100,1,-1):
#     for i in range(2,n):
#         if n%i == 0:
#             break
#         else:
#             print(n)
#             break

# 编写程序，输出有1,2,3,4组成的每位数都不相同的所有三位数
# 之所以不在 最里面的循环里进行判断 i,j,k都唯一，就是为了提高循环效率，减少不必要的循环次数
# digits = (1,2,3,4)
# ls = []
# for i in digits:
#     ii = i*100  # 百位数
#     for j in digits:
#         if j!= i:
#             jj = j*10
#         else:
#             continue
#         for k in digits:
#             if k != i and k != j:
#                 ls.append(ii+jj+k)
#             else:
#                 continue
# print(ls)

# # 不定参数的妙用
# def demo(**p):
#     for item in p.items():
#         print(item)
# demo(a=1,b=3,c=5) 
# # ('a', 1)
# # ('b', 3)
# # ('c', 5)
# # 传递参数时，序列解包  比如ls=[1,2,3],需要把它当作demo的三个参数依次传入，那么就 demo(*ls)即可----------------------
# # 同样 字典默认使用的键  items() 则使用键值对作为参数  values()则使用 值作为参数

