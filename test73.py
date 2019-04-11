#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月30日 18:13 
tip-->兴趣是最好的老师<--
"""
# 反向输出一个链表。
class ModiList():
    def __init__(self,length):
        self.length = length
    
    @property
    def createList(self):
        ls = []
        for i in range(self.length):
            inputDate = input("请输入第{}个值".format(i+1))
            ls.append(inputDate)
        return ls


if __name__ == '__main__':
    ls = ModiList(6)
    ls = ls.createList
    print(ls)
    ls.reverse()
    lst = ls
    print(lst)   
    # 我这里之所以打印出来的是 None，因为reverse直接翻转字符串本身