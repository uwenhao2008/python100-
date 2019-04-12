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
        ls = []
        sumidx = []
        for i in range(len(nums)):
            if nums[i] >= target:
                continue
            else:
                ls.append(nums[i])
        for i in range(len(ls)):
            # 这里要变为列表的拷贝，而不能是地址的引用 
            templs = ls[:]
            subtractor_a = ls[i]
            templs.pop(i)
            subtractor_b = target - subtractor_a
            if templs.count(subtractor_b) > 0:
                sumidx.append(nums.index(subtractor_a))
                sumidx.append(nums.index(subtractor_b))
                break
        print(sumidx)
        return sumidx

numlst = Solution()
numlst = numlst.twoSum([3,2,4],6)

