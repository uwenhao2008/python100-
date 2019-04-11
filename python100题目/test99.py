#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年04月11日 12:41 
tip-->兴趣是最好的老师<--
"""
# 有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
# test99_A.txt   test99_B.txt分别为此py文件对应调用处理的txt文档
ls = ['test99_A.txt','test99_B.txt']
def writeFile(fname):
    f = open(fname,'w',encoding='utf-8')
    rawInput = input("请往文件--{}--中输入需要保存的内容".format(fname))
    f.write(rawInput)
    f.close()

content = []
def readFile(fname):
    f = open(fname,'r',encoding='utf-8')
    fread = f.readlines()
    content.append(fread)
    f.close()

if __name__ == '__main__':
    for fname in ls:
        writeFile(fname)
        readFile(fname)
    # print(content)           #  [['asd '], ['asdwwq']]
    s = open('A+B.txt','w',encoding='utf-8')
    for i in content:
        s.write(i[0])
        s.write('\n')
    s.close()