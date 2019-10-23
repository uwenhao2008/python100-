#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月30日 15:31 
tip-->兴趣是最好的老师<--
"""
# 由于我是需要提交到leecode上的，所以导入一些内置库可能会失效，所以只能手动编写代码，
# 但是下面 https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001415616001996f6b32d80b6454caca3d33c965a07611f000
# 这个网址可以好好学习一些标准库，会极大的简化我的代码
# import itertools
# itertools.permutations
# 主要思路： 先将数值N中的每个数字独立存储并排序为list，长度记作n；在2的幂中找出长度为n的所有数值，
# 并同样对每个数字存储排序,得到list2，判断list与list2是否逐位相等
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        # 得到所有满足条件的幂函数列表，然后与N逐项对比  N排序以后对比
        ls = [str(2**i) for i in range(32)]
        # print(ls)
        for i in ls:
            if i == str(N):
                return True
            elif str(N) not in ls:
                return False

    def pers(self, N):
        # 用于存放符合要求的全排列
        lst = []
        ls = str(N)
        length = len(ls)
        if length == 0:
            print("参数N无效")
        elif length == 1:
            lst.append(N)
        else:
            for i in range(len(ls)):
                print("111--",i)
                for j in range(i):
                    print("222--",j)
    
s = Solution()

# print(s.reorderedPowerOf2(20))
print(s.pers(20))