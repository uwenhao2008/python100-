#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年03月26日 09:43 
tip-->兴趣是最好的老师<--
"""
# 编写input()和output()函数输入，输出5个学生的数据记录。
# 暂时不是用类的方式实现，先用传统思路，后续完善
from sys import stdout
# 使用类来编写
class StuData():
    def __init__(self,num):
        self.num = num

    @property
    def stu_input(self):
        student = []
        for i in range(self.num):
            student.append(['','',[]])
        for i in range(3):
            student[i][0] = input("请输入学生编号")
            student[i][1] = input("请输入学生姓名")
            for j in range(3):
                score = input("请以此输入语数外成绩")
                # student[i][2][j] = input("请以此输入语数外成绩")   # 这里这么写是错误的缘故，是因为空列表的添加只能使用append
                student[i][2].append(score)
        print(student)
        return student

    def stu_output(self,l):
        for i in range(len(l)):
            stuId = l[i][0]
            stuName = l[i][1]
            scoreYuwen = l[i][2][0]
            scoreMath = l[i][2][1]
            scoreEng = l[i][2][2]
            stdout.write('学生编号：{},姓名：{},语文成绩：{},数学成绩：{},英语成绩：{}\n'.format(stuId,stuName,scoreYuwen,scoreMath,scoreEng))
        print()

if __name__ == '__main__':
    l = StuData(3)
    ls = l.stu_input
    l.stu_output(ls)


'''
# 一般方法调用的写法
from sys import stdout
student = []
for i in range(3):
    student.append(['','',[]])
def stu_input():
    for i in range(3):
        student[i][0] = input("请输入学生编号")
        student[i][1] = input("请输入学生姓名")
        for j in range(3):
            score = input("请以此输入语数外成绩")
            # student[i][2][j] = input("请以此输入语数外成绩")   # 这里这么写是错误的缘故，是因为空列表的添加只能使用append
            student[i][2].append(score)
    print(student)
    return student

def stu_output(l):
    for i in range(len(l)):
        stuId = l[i][0]
        stuName = l[i][1]
        scoreYuwen = l[i][2][0]
        scoreMath = l[i][2][1]
        scoreEng = l[i][2][2]
        stdout.write('学生编号：{},姓名：{},语文成绩：{},数学成绩：{},英语成绩：{}\n'.format(stuId,stuName,scoreYuwen,scoreMath,scoreEng))
    print()

if __name__ == '__main__':
    l = stu_input()
    stu_output(l)
'''





