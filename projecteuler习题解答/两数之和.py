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
class Solution:
    def twoSum(self, nums,target):
        idxls = []
        for i in range(len(nums)):
            subtractor_a = nums[i]
            subtractor_b = target - subtractor_a
            if subtractor_a != subtractor_b:
                if nums.count(subtractor_b)>0:
                    idxls.append(nums.index(subtractor_a))
                    idxls.append(nums.index(subtractor_b))
            else:
                idxls.append(i)  
                for j in range(i+1,len(nums)-i):
                    if subtractor_a == nums[j]:
                        idxls.append(j)
                    break
                break
        print(idxls)
        return idxls

numlst = Solution()
# numlst = numlst.twoSum([2,5,5,11],10)
numlst = numlst.twoSum([3,2,4],6)

