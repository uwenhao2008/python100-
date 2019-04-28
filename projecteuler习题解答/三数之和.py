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
    def twoSum(self, nums, target):
        print(nums)
        ls = []
        count = 0       # ls二维数组序列
        # 倒序循环
        for i in range(len(nums)-1,0,-1):
            templs = nums[:]
            # 这里的templs ！= nums  why？  找到缘故了，是因为我调试的时候，监视器里有一句代码templs.pop(i),导致了这个问题
            templs.pop(i) # 其实就是nums[i]     
            # 莫非是位置放的不对？需要在for里  我知道哪里错了，list.pop()返回的是扔出去的值
            # 原因不是这个，是因为遍历途中删除项目大的时候，后面的项目会填充之前的，造成跳过
            # 三种方法 1.倒序， 2.遍历拷贝的list，操作原始的list 3.通过wyile，i--的方式
            for j in range(len(templs)-1,0,-1):
                # templs 长度变化的时候，len(templs)-1 可能会溢出，因为存在 j=5而len(templs)长度不够5的情况
                template = templs[:]
                temp = templs[j]
                subtractor_c = 0-nums[i]-temp
                template.pop(j)
                # else:
                #     print("弹尽粮绝")
                #     break
                # templs.remove(templs[j])
                if template.count(subtractor_c) != 0:
                    ls.append([])
                    ls[count].append(nums[i])
                    ls[count].append(temp)
                    ls[count].append(subtractor_c)
                    
                    # templs.remove(nums[i])   此处不要remove，因为开头已经pop了 
                    templs.remove(temp)
                    templs.remove(subtractor_c)
                    # 第20行代码，pop了一个值，所以这里就少了
                    print(templs)
                    nums = templs
                    count += 1

        print(ls)


        

a = Solution()
a.threeSum([-1, 0, 1, 2, -1, -4])