#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月01日 18:49 
tip-->兴趣是最好的老师<--
"""
# 海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
# 第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，
# 第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
'''
# 蛮力的方式
def monkeyMath():
    n=0
    ls = []
    while(1):
        n += 1
        if n%5 == 1:
            if ((n-1)*0.8)%5 == 1:
                if (((n-1)*0.8-1)*0.8)%5 == 1:
                    if ((((n-1)*0.8-1)*0.8-1)*0.8)%5 == 1:
                        if (((((n-1)*0.8-1)*0.8-1)*0.8-1)*0.8)%5 == 1:
                            print(n)
                            ls.append(n)
        if len(ls) == 10:
            print(ls)
            break
monkeyMath()
'''

'''
# 取巧的方式 递归
def monkeyMath(n):
    if n%5 == 1:
        return n
    elif ((n-1)*0.8)%5 == 1:
        return monkeyMath(n-1)
'''

'''
我这里不明白下main代码的含义
'''
if __name__ == '__main__':
    # x代表最开始的桃子数的桃子数
    i,j,x = 0,1,0
    while i<5:
        x = 4*j
        for i in range(0,5):
            if (x%4 != 0):
                break
            else:
                i += 1
            x = x/4*5+1
        j += 1
    print(x)