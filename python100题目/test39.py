#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月24日 00:53 
tip-->兴趣是最好的老师<--
"""
# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
ls = [1,3,4,6,8,12,21,27,33,46]
# rawInput = int(input("输入需要插入的数据"))
rawInput = 15

"""
思路：# 使用二分法查找 对应的序号
函数返回 data的index,flsg==0，lst递增，flag==1，lst递减 
其实这里不要用flag这么麻烦，把列表都处理为递增就可以让方法统一了，要不很繁杂
"""
def binarySearch(lst,data):
    flag = 0   # 0代表递减
    if lst[0]>=lst[-1]:
        flag = 1
    low,high = 0,len(lst)
    while True:
        midIdx = (low+high)//2
        if high - low == 1:
            print('真相只有一个',high)
            break	  
        # lst 递增的情况  我这只考虑递增的情况。lst先处理为递增然
        if flag == 0:
            if lst[midIdx] < data:
                low = midIdx
            elif lst[midIdx] > data:
                high = midIdx
            print(ls[low:high])

binarySearch(ls,23)
  
