#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
"""
# 输入三个整数x,y,z，请把这三个数由小到大输出。
# rawdata = input("请输入三个数，逗号间隔")
# listdata = list(map(lambda x:int(x),rawdata.split(',')))
'''
def sortNum(x,y):
    if x>=y:
        return 1
    else:
        return -1

# 自己还是太low了，思路不清楚
def bubble(lst):
    if isinstance(lst,list):
        # for idx,item in enumerate(lst):
            # 用另外的len遍历列表   highIdx = lst[idx+1]就不会错误了
        for idx in range(len(lst)):
            # 不交换位置
            lowIdx = lst[idx]
            # 超出len报错
            highIdx = lst[idx+1]
            if sortNum(lowIdx,highIdx)>0:
                pass
            else:
                temp = lowIdx
                lst[idx] = highIdx
                lst[idx+1] = temp
                print(lst)
                
    else:
        print("参数lst不是列表类型")
bubble([1,4,2,55,3,45,67])
'''
# 冒泡算法
def bubble_sort(nums):
    if isinstance(nums,list):
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]  
                    print(nums)
    else:
        print("参数类型不对")

bubble_sort([1,4,2,55,3,45,67])