#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月11日 14:36 
tip-->兴趣是最好的老师<--
"""
# 列表转换为字典。
# ls_a = ['name','age']
# ls_b = ['wen',33]
# # 最傻瓜最NB的方式   但是只能处理 ['a','b']len为2的数据   
# ds = dict([ls_a,ls_b])
# print(ds)
# {'name': 'age', 'wen': 33}

'''
# 相对完美的方式
ls_a = ['name','age','sex']
ls_b = ['wen',33,'male']
ds = dict().fromkeys(ls_a)
dslen = len(ds)
print(dslen)
for i in range(dslen):
    ds[ls_a[i]] = ls_b[i]
print(ds)
'''

# 再设想一种使用多维矩阵的方式
ls_a = ['name','age','sex']
ls_b = ['wen',33,'male']
ls = [ls_a,ls_b]
print(ls)
dictList = []
for i in range(len(ls_a)):
    dictList.append([])
    for j in range(len(ls)):
        dictList[i].append(ls[j][i])
print(dictList)
print(dict(dictList))
# 终于完成了100题目，开始自己的下一阶段的历练


# ds = dict.fromkeys(ls_a,ls_b)   # {'name': ['wen', 33, 'male'], 'age': ['wen', 33, 'male'], 'sex': ['wen', 33, 'male']}
# ds = dict.fromkeys(ls_a,10)   # {'name': 10, 'age': 10, 'sex': 10}
# ds = {}
# ds = ds.fromkeys(ls_a)
# print(ds)