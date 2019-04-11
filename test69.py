#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月25日 17:14 
tip-->兴趣是最好的老师<--
"""
# 有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
# 
# 其他思路，可以使用list.pop方法
#           list.insert()
# 
# 这道题不简单~~~
# from collections import deque    高级用法
ls = list(range(10))
# b = deque(a)
# b.rotate
def luckboy(ls,step=3):
    temp = ls[:]
    l = len(temp)
    while l>=2:
        nextloop = []
        print('数据源->',temp)
        times3 = l//step
        if times3 >= 1:
            leavesIndex = 3*times3
            print('此刻times3------------------',times3)
            for i in range(l):
                if (i+1)%3 == 0:
                    nextloop.append(temp[i-2])
                    nextloop.append(temp[i-1])
                    print('跳步3->',nextloop)
            temp = temp[leavesIndex:]
            print('剩余碎片->',temp)
            temp.extend(nextloop)
            # 我这里不需要引入一个j，因为列表每次都是从0开始数就可以
            j = l-leavesIndex
            l = len(temp)
            print('新数据源----->',temp,'新j为---',j)
        else:
            # 当列表只有2个值的时候，特殊处理   [a,b] 留下的是b
            # print(temp[-1])
            break
    return temp[-1]

luckNum = luckboy(ls,3)  
# 下面这种方式是打印出luckNum的内存地址，而他刚好保存的是def luckboy
print(luckboy)
print(luckboy(ls,3))

        


    