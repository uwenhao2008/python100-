#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年11月07日 15:06 
tip-->兴趣是最好的老师<--
https://blog.csdn.net/sunny1235435/article/details/95733370
要求：
1.小船最多只能坐两个
2.任何时候，只要某一岸妖怪数量 > 和尚数量，和尚就会被吃掉
3.小船是有状态的  LOCAL or REMOTE

# 心得：
自己实现了，花了三天时间，其实调试错误花费的时间最多，尤其是searchReault()函数最后的pop最为经典，能否进行深度遍历就看他了
还有就是自己一开始的record定义哪里花费了很多时间  想实现[[1],[2],[3]] 但是总得到的是[[1,2,3]]  这个地方看看不适用deque只是使用数组能否实现
record = initial  和 record = list(initial)  之间的差别
"""
from collections import deque
# [左岸和尚，左岸妖怪，右岸和尚，右岸妖怪，小船位置REMOTE或LOCAL] 来表示状态
# 这里反映出来我的一个思路误区，我思维深处把船上的和尚或妖怪数量也当作了一种状态，这么考虑会把问题复杂化，让问题停留在0-1状态，而不要出现中间态，这不是量子编程  def QS_next_state()函数
# 我最初设计的状态为 [左岸和尚,左岸妖怪,右岸和尚,右岸妖怪,船上和尚,船上妖怪,船方向] 如此设计的话就把问题复杂化了
initial_state = [3,3,0,0,'LOCAL']
final_state = [0,0,3,3,'REMOTE']
num = 0    # 方法总数
record_list = [[list(initial_state)]]   # 过程序列


# [过河动作，小船走向，左岸和尚变化数量，左岸妖怪变化数量]
action_effect = [['ONE_MONSTER_GO','REMOTE',0,-1],['TWO_MONSTER_GO','REMOTE',0,-2],['ONE_MONK_GO','REMOTE',-1,0],['TWO_MONK_GO','REMOTE',-2,0],['ONE_MONSTER_ONE_MONK_GO','REMOTE',-1,-1],
                 ['ONE_MONSTER_BACK','LOCAL',0,1],['TWO_MONSTER_BACK','LOCAL',0,2],['ONE_MONK_BACK','LOCAL',1,0],['TWO_MONK_BACK','LOCAL',2,0],['ONE_MONSTER_ONE_MONK_BACK','LOCAL',1,1]]

def next_state_lawful(current_state,action):
    # 判断action合法性
    # 1，如果左岸没有和尚了，一切从左岸运和尚去右岸的动作都不合法(不用这么考虑，只要左岸和尚+船上和尚 在0~3就是正常的)
    # 2. 如果船再对岸，那么以切从左岸往右岸运送的动作都非法

    # 船在左岸，则从右岸往左岸的动作都非法
    if current_state[4] == action[1]:
        return False
    # 左岸和尚(妖怪)为空的时候，不能出现往对岸运送和尚的动作 或 右岸和尚加船上和尚>3也是非法的
    if current_state[0]+action[2]<0 or current_state[0]+action[2]>3:
        return False
    # 判断运送妖怪动作的合法性
    if current_state[1]+action[3]<0 or current_state[1]+action[3]>3:
        return False
    return action

def QS_next_state(current_state,action_effect):
    for action in action_effect:
        # next_state合法
        if next_state_lawful(current_state,action):
            next_state = []
            # state:[左岸和尚，左岸妖怪，右岸和尚，右岸妖怪，小船位置REMOTE或LOCAL]
            # action:[过河动作，小船走向，左岸和尚变化数量，左岸妖怪变化数量]
            # next_state左岸的和尚
            next_state.append(current_state[0] + action[2])
            # next_state左岸的妖怪
            # next_state[1] = current_state[1] + action[3]
            next_state.append(current_state[1] + action[3])
            # next_state右岸的和尚   因为离开左岸记为负数，所以用减法
            next_state.append(current_state[2] - action[2])
            # next_state右岸的妖怪
            next_state.append(current_state[3] - action[3])
            # next_state 船的状态
            next_state.append(action[1])
        # next_state 不合法，那么下一个状态就是当前状态
        else:  
            next_state = current_state
        # 这里的yield因为在for循环里，所以就可以进行树的遍历了~~~~~~~~~~~~
        yield next_state


record = deque()
record.append(initial_state)
def searchReault(record, final_state, action_effect):
    global num,record_list
    # 这里错了，导致所有的current_state都是同一个 
    # 因为我以前写的是 current_state = list(record[-1])，这个是深拷贝，而不是引用~~~
    current_state = record[-1]    #！！！！！！！！！
    next_state = QS_next_state(current_state,action_effect)

    # 这里的state其实就是 生成器生成函数的返回值next_state
    for state in next_state:
        # 满足任意一岸 和尚数量>=妖怪数量 record进行追加 或者只有妖怪没有和尚
        # 就判断左岸，右岸状态，不要考虑船再运送中的状态~~~
        # (左岸和尚数量 >= 左岸妖怪 or 左岸没有和尚)  and  (右岸和尚数量 >= 右岸妖怪 or 右岸没有和尚)
        # [左岸和尚，左岸妖怪，右岸和尚，右岸妖怪，小船位置REMOTE或LOCAL]
        # 我这里条件判断可能有问题~~~~~~~~
        if (state[0]>=state[1] or state[0]==0) and (state[2]>=state[3] or state[2]==0):
            if state not in record:   # 防止进入死循环
                record.append(state)
                # 得到最终状态，同时船在 REMOTE  直接些stata == final_state,不用写record[-1]
                if state == final_state and state[4] == 'REMOTE':
                    print(record)
                    record_list.append(record)
                    num += 1
                # 递归调用
                else:
                    # 若是出现死循环，pop history_record的最后一位
                    # record = list(history_record[-1])   # 我这里写错了,写为了list(history_record)[-1]
                    searchReault(record, final_state, action_effect)
                # 为什么pop要写在这个位置呢？？？   因为上一行是递归调用自己，也就意味着函数内部所有状态遍历完以后
                # 去除当前循环中添加的状态，若没有这一句那么就无法进行深度遍历了，因为树枝就消失了....
                # 我这里之所以糊涂了就是因为，当前位置实在一个循环里，循环过程中发现满足条件就把当前record打印出来，但是要保证下一个state接着扫描其他树枝，所以这里一定要pop，否则就不会是一个完整的树了
                record.pop()
        

searchReault(record, final_state, action_effect)
    