#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年11月13日 10:48 
tip-->兴趣是最好的老师<--
https://blog.csdn.net/zhanshen112/article/details/100687608
"""
class GPS:
	def __init__(self):
		pass
	def struct(self,idx,px,py,vx,vy):
		self.idx=idx
		self.px=px
		self.py=py
		self.vx=vx
		self.vy=vy
Data=[]
print(Data)
for i in range(2):
	Data.append(GPS())
# Data=[GPS(),GPS()]
Data[0].idx='00'
Data[0].px=1.1
Data[0].py=1.2
Data[0].vx=1.3
Data[0].vy=1.4
Data[1].idx='01'
Data[1].px=1.5
Data[1].py=1.6
Data[1].vx=1.7
Data[1].vy=1.8
print(Data[0].idx,Data[1].idx)
# 结构体可以理解为序列,如下图所示
# [<__main__.GPS object at 0x00000180B7F743C8>, <__main__.GPS object at 0x00000180B7F74668>]
print(Data)

# # 下面是一个应用的实例：
# # 在编程中经常会遇到对数组元素进行交换，当交换并处理后，需要按原始位置输出时，可以使用结构体来简化编程。
# # 例如，对一组整数的最大元素加上次大元素的值，次大元素加上第三大元素的值，第三大元素加上第四大元素的值……最小元素加0，依次对每一个元素进行处理，
# # 处理完成后按照原始数组的元素位置输出处理结果。
# # 分析：使用类创建结构体，使用列表创建结构体数组。稳定性排序与idx有关。
# class mydata():
# 	def __init__(self):
# 		pass
# 	def struct(self,value,idx):
# 		self.value=value
# 		self.idx=idx

# #输入的数字个数
# n=eval(input())

# # 输入数字大小
# struct=[]
# for i in range(n):
# 	struct.append(mydata())
# str_input=input()
# str_input=str_input.split(" ")
# for i in range(n):
# 	struct[i].value=eval(str_input[i])
# 	struct[i].idx=i

# # 数字处理
# for i in range(n):
# 	for j in range(0,n-1-i):
# 		if struct[j].value<struct[j+1].value:
# 			struct[j],struct[j+1]=struct[j+1],struct[j]
# for i in range(n):
# 	if i<n-1:
# 		struct[i].value=struct[i].value+struct[i+1].value
# 	else:
# 		pass
# for i in range(n):
# 	for j in range(n):
# 		if i!=struct[j].idx:
# 			continue
# 		else:
# 			print("{}".format(struct[j].value),end=" ")
# 			break


class Test():
    def __init__(self):
        self.name = 123

test = Test().name
print(test)