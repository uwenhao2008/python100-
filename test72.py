#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月30日 18:04 
tip-->兴趣是最好的老师<--
"""
# 创建一个链表。
class modifyList():
    def __init__(self,length):
        self.length = length

    def createList(self):
        ls = []
        for i in range(self.length):
            inputDate = input("请输入第{}个数据".format(i+1))
            ls.append(inputDate)
        return ls

if __name__ == '__main__':
    ls = modifyList(6)
    print(ls.createList())