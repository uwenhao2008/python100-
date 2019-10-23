#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月13日 01:13 
tip-->兴趣是最好的老师<--
"""
'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
'''
class Solution:
    def threeSum(self, nums, target):
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            left = i+1
            right = n-1
            while left < right:
                cur_num = nums[left]+nums[right]+nums[i]
                if cur_num == 0:
                    # ls = [nums[i], nums[left], nums[right]]
                    ls = [i, left, right]
                    res.append(ls)
                    if right - left > 1:
                        left += 1
                        right -= 1
                    elif right - left == 1:
                        break
                elif cur_num > 0:
                    right -= 1
                else:
                    left += 1
        # res = list(set([tuple(t) for t in res]))
        res = [list(x) for x in res]
        print(res)
        return res

a = Solution()
# a.threeSum([-1, 0, 1, 2, -1, -4],0)
a.threeSum([0,0,0,0,0],0)
# 上卖弄这种特殊情况程序没有实现，找原因
# a.threeSum([-1, 0, 1, 2, -1, -4],0)