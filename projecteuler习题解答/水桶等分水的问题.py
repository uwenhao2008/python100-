#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年10月25日 17:01 
tip-->兴趣是最好的老师<--
问题描述：有三个水桶，分别可以装8L，5L，3L，已知8L水桶是装满水的，只使用这三个水桶最终实现把水分为两份，输出分水过程
https://blog.csdn.net/sunny1235435/article/details/95614764
"""
from collections import deque

initial_backet_state = [0,0,8]    # 水桶初始状态
bucket_volume = [3,5,8]           # 水桶容量

# 利用python的deque队列记录状态转移情况，初始化时加入水桶初始状态。deque是可以从头尾插入和删除的队列，在不指定大小时，为一个无边界的队列
record = deque()
record.append(initial_backet_state)

def next_state_lawful(current_state,bucket_volume):
    #通过列表推导式获得下一动作的二元组构成的列表，由（倒出水的容器编号，倒入水的容器编号）组成。
    #二重循环得到下一步的所有可能动作，然后通过1.倒入倒出不能为同一个2.倒出的捅中必须有水3.倒入的桶中不能为满 的条件判断是否合法
    next_action = [(from_, to_) for from_ in range(3) for to_ in range(3) if from_ != to_ and current_state[from_] > 0 and current_state[to_] < bucket_volume[to_] ]
    
    for from_,to_ in next_action:
        # next_state = current_state #浅复制造成错误   浅复制id()是相同的
        next_state = list(current_state)
        # from_ 编号的水桶不能完全倒入 to_ 编号的水桶
        if current_state[from_] + current_state[to_] > bucket_volume[to_]:
            next_state[from_] -=(bucket_volume[to_] - current_state[to_])
            next_state[to_] = bucket_volume[to_]
        else:
            next_state[from_] = 0
            next_state[to_] = current_state[to_] + current_state[from_]

        #再由所有可能的合法动作得出所有的下一个状态，通过yield产生供其它函数调用。
        yield next_state

num = 0
record_list = []
#记录调试的变量：num表示总共实现方法数，record_list记录所有实现路径

def searchResult(record, bucket_volume=[3,5,8], final_bucket_state=[0,4,4]):
    # global 可以为函数外部的变量赋值
    global num, record_list
    #由record的末尾元素得到当前水桶状态
    current_state = record[-1]
    #得到关于当前状态的下一状态的可迭代生成器，供下一步循环使用
    next_state = next_state_lawful(current_state, bucket_volume)

    # 遍历所有可能的下一步状态
    for state in next_state:
        if state not in record:
            #保证当前状态没在以前出现过。如果状态已经出现还进行搜索就会形成状态环路，陷入死循环
            #保证当前状态没在以前出现过。如果状态已经出现还进行搜索就会形成状态环路，陷入死循环。
            record.append(state)
            #添加新的状态到列表中
            if state == final_bucket_state:
                print(record)
                #打印出可行方案
                #record_list.append(record)这样使用错误，导致加入列表的是record的引用，应该使用下面的式子来进行深复制，得到一个新的队列再加入列表。
                record_list.append(deque(record))
                num += 1
            else:
                # 递归搜索
                searchResult(record, bucket_volume, final_bucket_state)
            # 去除当前循环中添加的状态，进入下一个循环，关键步，第一次实现的时候遗漏了   
            record.pop()
   

searchResult(record, bucket_volume=[3,5,8], final_bucket_state=[0,4,4])