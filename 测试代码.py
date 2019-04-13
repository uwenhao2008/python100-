#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月11日 14:16 
tip-->兴趣是最好的老师<--
"""

# ls = [['a','b',3],[2,3,33],["Hello KT",328,{"name":"POP",'age':28}]]
# print(ls)
# for i in ls:
#     print(i[2])

# ds = {'name':'wen','age':28}
# ds['name'] = 'hao'
# print(ds)

# ls1,ls2 = ['x','y'],[3,8]
# print(dict([ls1,ls2]))

# d = dict()
# hashmap = {0:'a',1:'b',2:'c',3:'d'}
# # a = hashmap.pop(1)
# a = iter(hashmap)
# print(a)
# print(str(a))


# # 非常好的包 !!!!!!!!!!
# import collections 
# p = collections.deque(maxlen=3)
# p.append(1)
# p.append(2)
# p.append(3)
# p.append(66)
# # p.pop()
# # p.insert(2,89)
# print(list(p))

# dict = {"a" : "apple", "b" : "banana"}
# dict2 = {"c" : "grape", "d" : "orange"}
# dict.update(dict2)
# print(dict)
# 以上等价于
# D = {"key1" : "value1", "key2" : "value2"}
# E = {"key3" : "value3", "key4" : "value4","key2" : "value6"}
# # 存在重复key的情况，对应的key被替换了
# for k in E:
#     D[k] = E[k]
# print(D)

# #调用sorted()排序
# dict = {"a" : "apple", "b" : "grape", "c" : "orange", "d" : "banana"}
# #按照key排序    不要把这里的sort了list里的排序弄混了
# print(sorted(dict.items(), key=lambda d: d[0]))
# #按照value排序
# print(sorted(dict.items(), key=lambda d: d[1]))

# # 字典初始化  2中方式
# # p = dict(name='visaya', age=20)
# p = dict(zip(['name','age'],['wen','male']))
# print(p)


# # 字典的高级用法
# d = dict.fromkeys(['a', 'b'], 1)
# print(d)
# # dict.keys()类似信使可以进行交集和并集等集合操作（类似集合，因为不存在重复的项），但dict.values()不可以进行如上操作
# k = d.keys()
# print(k)
# print(list(k))
# print(k | {'x': 3})
# print(k)
# print( k | {'x', 'y'})
# print("^--^",k & {'x'})   # 因为交集为空，所以猜得到set()的

# 字典copy()
d = {"name":"nico", "age":23}
d1 = d.copy()
print(d1)
d['sex'] = 'male'
d2 = d1.items()
print('-->',d2)
print('d',d)
print('d1',d1)
# 有key为name
print(d.pop('name','Wen'))
# 没有key为names
print(d.pop('names','Wen'))

