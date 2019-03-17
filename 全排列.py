#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
"""
# 题目要求很简单，输入n个数，能自动打印出全排列（Permutation）。比如输入1，2，3，那它的全排列就是123，132，213，231，312，321。
rawInput = input("请输入n个数，逗号间隔")
# lstNums = list(map(lambda x:int(x),rawInput.split(',')))
lstNums = rawInput.split(',')

ls = []
'''
递归思想：
取出数组中第一个元素放到最后，即a[1]与a[n]交换，然后递归求a[n-1]的全排列

1）如果数组只有一个元素n=1，a={1} 则全排列就是{1}
2）如果数组有两个元素n=2，a={1,2} 则全排列是：
{2,1}--a[1]与a[2]交换。交换后求a[2-1]={2}的全排列，归结到1)
{1,2}--a[2]与a[2]交换。交换后求a[2-1]={1}的全排列，归结到1)
3）如果数组有三个元素n=3，a={1,2,3} 则全排列是
{{2,3},1}--a[1]与a[3]交换。后求a[3-1]={2,3}的全排列，归结到2）
{{1,3},2)--a[2]与a[3]交换。后求a[3-1]={1,3}的全排列，归结到2）
{{1,2},3)--a[3]与a[3]交换。后求a[3-1]={1,2}的全排列，归结到2）
--------------------- 
作者：data_heng 
来源：CSDN 
原文：https://blog.csdn.net/zhoufen12345/article/details/53560099 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
def permutation(lst):
    for i in range(len(lst)):
        lst[1],lst[-1] = lst[-1],lst[1]
        
'''
def permutation(lst):
    length = len(lst)
    ls.append(''.join(lst))
    for i in range(length-1):
        for j in range(i+1,length):
            tempList = lst
            lst[i],lst[j] = tempList[j],tempList[i]
            ls.append(''.join(lst))
            permutation(lst)
    print(ls)     
'''
'''
def permutation(lst):
    ls = []
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            lst[i],lst[j] = lst[j],lst[i]
            print(lst)
'''
permutation(lstNums)