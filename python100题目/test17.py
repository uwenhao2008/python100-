#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月18日 22:22 
tip-->兴趣是最好的老师<--
"""
# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,   ！！！！！！

# rawInput = input('输入任意一串字符：')
rawInput = 'abc 1238A15.388DDsss+- //~'

ls = {"num":0,"str":0,"blank":0,"other":0}
# 思路一：通过正则筛选，然后分别统计
# 不能使用正则，因为不是匹配规则


# 思路二：直接统计   通过asicc判断   通过字符串的单独方式判断数字、字母等
# 通过asicc
# print( 'c', ord('c'))

# 通过字符串的特殊方法
'''
def staticDatetype(lst):
    for c in lst:
        if c.isalpha():
            # ls.get('str') += 1   这里就会报错，因为字典的赋值不是这么操作的
            ls['str'] = ls.get('str')+1
        elif c.isdigit():
            ls['num'] = ls.get('num')+1
        elif c.isspace():
            ls['blank'] = ls.get('blank')+1
        else:
            ls['other'] = ls.get('other')+1

staticDatetype(rawInput)
print(ls)
'''
