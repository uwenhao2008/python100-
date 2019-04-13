#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月11日 16:40 
tip-->兴趣是最好的老师<--
"""
'''
https://leetcode-cn.com/problems/two-sum/
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

新语法解释参见  https://blog.csdn.net/sunt2018/article/details/83022493
'''

'''
class Solution:
    def twoSum(self, nums,target):
        idxls = []
        istart = 0
        length = len(nums)
        for i in range(length):
            subtractor_a = nums[i]
            subtractor_b = target - subtractor_a
            for istart in range(1+i,length):
                if nums[istart] == subtractor_b:
                    idxls.append(i)
                    idxls.append(istart)
        print(idxls)
        return idxls

numlst = Solution()
# numlst = numlst.twoSum([2,5,5,11],10)
numlst = numlst.twoSum([3,2,4],6)
# numlst = numlst.twoSum([3,2,3],6)
'''

# 通过hash表来解决，即python的字典
class Solution:
    def twoSum(self, nums,target):
        ls = []
        for idx,item in enumerate(nums):
            ls.append([])
            ls[idx].append(idx)
            ls[idx].append(item)
        hashmap = dict(ls)
        templist = list(hashmap.keys())
        # i为字典对应的key
        tempId = []
        for i in templist:
            tempdict = hashmap.copy()
            subtractor_a = hashmap.get(i)
            subtractor_b = target - subtractor_a
            del tempdict[i]
            if subtractor_b in tempdict.values():
                tempId.append(i)
        print(tempId)



numlst = Solution()
numlst = numlst.twoSum([3,2,3,5,5,7,7],14)