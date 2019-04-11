#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月21日 16:03 
tip-->兴趣是最好的老师<--
"""
"""
------------------------------------------------------
思路：可以通过ord(a) 转换 ascii来编程
------------------------------------------------------
"""
# 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
# 笔算的结果应该是  az bx cy
teamA = ['a','b','c']
teamB = ['x','y','z']
def findList():
    for ia,itemA in enumerate(teamA):
        for ib,itemB in enumerate(teamB):
            if ia!=ib:
                print(ia,itemA,'--VS--',ib,itemB)

                # a不和x比，c不和x，z比
                if not (ia==0 and ib==0 or ia==2 and ib==0 or ia==2 and ib==2):
                    # c和y比  y就不能和a、b比了
                    if not (ia==0 and ib==1 or ia==1 and ib==1):
                        print(ia,itemA,'--VS--',ib,itemB)
                        # a和z b和xz c和y  如何进一步判断？
            
            # 我这里为什么要搞两个变量呢？abc固定，另外一个变不可以吗？

findList()


# def f():
#     for i in range(5):
#         for j in range(5):
#             if i!=j:
#                 print(i,j)

# f()