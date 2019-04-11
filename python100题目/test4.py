#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
"""
# 输入某年某月某日，判断这一天是这一年的第几天？
t = input("请用'-'间隔输入年月日：")
temptime = t.split('-')
# reduce(lamda str_to_int: int(str),dtime)   reduce 需要两个参数
dtime = list(map(lambda x:int(x),temptime))

# 判断是否是闰年
def isLeapYear(y):
    y = int(y)
    if y%400==0 and y%4==0 and y%100!=0:
        print("因为是闰年，所以天数+1")
        return True

'''
# 写法1
# 只有闰年2月多一天
mondays = [31,59,90,120,151,181,212,243,274,305,335,365]   # 我这里1月当做0，会简化很多代码！！！
# mondays = [31,28,31,30,31,30,31,31,30,31,30,31]   #   通过reduce遍历  这个思路试一试
days = 1 if isLeapYear(dtime[0]) else 0
# 一月的时候  直接计算 dtime[2]
if dtime[2] == 1:
    print("{}是今年的第{}天".format(dtime,dtime[2]))
else:  
    mdays = mondays[dtime[1]-2]+dtime[2]+days
    print("{}是今年的第{}天".format(dtime,mdays))
'''


# 只有闰年2月多一天

mondays = [31,28,31,30,31,30,31,31,30,31,30,31]   #   通过reduce遍历  这个思路试一试
def add(x,y):
    return x+y
days = 1 if isLeapYear(dtime[0]) else 0
# 一月的时候  直接计算 dtime[2]
from functools import reduce  #reduce需要单独导入使用
if dtime[2] == 1:
    print("{}是今年的第{}天".format(dtime,dtime[2]))
elif dtime[2] == 2:
    print("{}是今年的第{}天".format(dtime,dtime[2]+31))
else:  
    newdays = mondays[:dtime[1]-1]
    mdays = reduce(add,newdays)+dtime[2]
    print("{}是今年的第{}天".format(dtime,mdays))



"""
# 我自己的思路太混乱了，优秀的编程是把问题简单化，而不是为了显示语法的高超而自找麻烦
# 1月大2月小 顺口溜，闰年的时候 2月只有29天，平常2月默认28天
mon = [1,0,1,-1,1,-1,1,1,-1,1,-1,1]
days = 0
if isLeapYear(dtime[0]):
    mon_2_days = 29  # 闰年29天
else:
    mon_2_days = 28    
for idx in range(0,dtime[1]):
    mon_days = (31 if mon[idx]>0 else 30)   # 根据大小约判断当月天数
    days += (31 if mon[idx]>0 else 0)
    if idx >= 2:
        days += mon_2_days
print(days+dtime[2])
"""


