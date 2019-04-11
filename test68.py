#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月25日 16:52 
tip-->兴趣是最好的老师<--
"""
# 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
# 思路1：直接转字符串，然后采用切割拼接的方式，这个方法太容易，所以我换一个方式试一试

# 采用循环遍历转换下标的方法
ls = [1,2,3,4,5,6,7,8,9,10]

def revList(ls,m_start):
    l = len(ls)
    for idx in range(m_start):
        ls[idx],ls[l-m_start+idx] = ls[l-m_start+idx],ls[idx]
        print(ls)
    return ls

if __name__ == '__main__':
    revList(ls,4)
    print(ls)