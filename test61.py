#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月25日 10:30 
tip-->兴趣是最好的老师<--
"""
# 打印出杨辉三角形（要求打印出10行如下图）。
'''
1 
1   1 
1   2   1                         i=2,j=2    ls[i][j] = ls[i-1][j]+ls[i-1][j-1]
1   3   3    1                    i=3,j=2  
1   4   6    4    1 
1   5   10   10   5    1 
1   6   15   20   15   6    1 
1   7   21   35   35   21   7    1 
1   8   28   56   70   56   28   8   1 
1   9   36   84   126  126  84   36  9   1
'''
from sys import stdout
def pascalTrangle(lines):
    ls = []
    for i in range(lines):
        ls.append([])
        for j in range(i+1):
            sum = 0
            if i == 0 or i == 1:
                ls[i].append(1)
            else:
                # i>=2
                # if not j==1 or j==i+1:
                if j == 0 or j == i:
                    ls[i].append(1)
                else:
                    sum = ls[i-1][j]+ls[i-1][j-1]
                    ls[i].append(sum)
    return ls       

if __name__ == '__main__':
    l = pascalTrangle(10)
    for i in range(len(l)):
        print(l[i])
# 思考  这里使用 stdout.write() 和print()来进行一下输出美化工作
