#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年06月21日 15:32 
tip-->兴趣是最好的老师<--
"""
# 功能：sys.modules是一个全局字典，该字典是python启动后就加载在内存中。每当程序员导入新的模块，
# sys.modules将自动记录该模块。当第二次再导入该模块时，
# python会直接到字典中查找，从而加快了程序运行的速度。它拥有字典所拥有的一切方法。
import sys
print(sys.modules.keys)
print(sys.modules.keys())
print(sys.modules.values)
print(sys.modules.values())
print(sys.modules["os"])