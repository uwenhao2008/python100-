#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年10月25日 17:01 
tip-->兴趣是最好的老师<--
问题描述：有三个水桶，分别可以装8L，5L，3L，已知8L水桶是装满水的，只使用这三个水桶最终实现把水分为两份，输出分水过程
"""
from collections import deque

initial_backet_state = [0,0,8]    # 水桶初始状态
backet_volume = [3,5,8]           # 水桶容量

# 利用python的deque队列记录状态转移情况，初始化时加入水桶初始状态。deque是可以从头尾插入和删除的队列，在不指定大小时，为一个无边界的队列
record = deque()
record.append(initial_backet_state)

def next_state_lawful(current_state,backet_volume):
    #通过列表推导式获得下一动作的二元组构成的列表，由（倒出水的容器编号，倒入水的容器编号）组成。
    #二重循环得到下一步的所有可能动作，然后通过1.倒入倒出不能为同一个2.倒出的捅中必须有水3.倒入的桶中不能为满 的条件判断是否合法
    next_action = [(from_, to_) for from_ in range(3) for to_ in range(3) if from_ != to_ and current_state[from_] > 0 and current_state[to_] < backet_volume[to_] ]
    
    for from_,to_ in next_action:
        # next_state = current_state #浅复制造成错误   浅复制id()是相同的
        next_state = list(current_state)
        # from_ 编号的水桶不能完全倒入 to_ 编号的水桶
        if current_state[from_] + current_state[to_] > backet_volume[to_]:
            next_state[from_] -=(backet_volume[to_] - current_state[to_])
            next_state[to_] = backet_volume[to_]
        else:
            next_state[from_] = 0
            next_state[to_] = current_state[to_] + current_state[from_]

        #再由所有可能的合法动作得出所有的下一个状态，通过yield产生供其它函数调用。
        yield next_state





