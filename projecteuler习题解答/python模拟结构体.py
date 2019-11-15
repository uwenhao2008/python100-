#!/usr/bin/python

import sys

class MyClass():
    def __init__(self, name = ""):
        self.name = name
        self.data_dic = {}
        self.index = -1

    class Struct():
        def __init__(self, contents, name, message, status, num = -1):
            self.contents = contents
            self.name = name
            self.message = message
            self.status = status
            self.line_num = num
    #return struct item.
    def make_struct(self, contents, name, message, status, num = -1):
        return self.Struct(contents, name, message, status, num)
    
    class StructList():
        def __init__(self, contents, name, message, status, num = -1):
            self.contents = contents
            self.name = name
            self.message = message
            self.status = status
            self.line_num = num
    #return struct item.
    def make_structlist(self, contents, name, message, status, num = -1):
        return self.StructList(contents, name, message, status, num = -1)

if __name__ == "__main__":
    test = MyClass()
    print(test.make_struct("hello world","s2","你好","success"))
    print(test.make_struct("hello world","s2","你好","success").name)
    print(test.make_struct("hello world","s2","你好","success"))
    print(test.make_struct("hello world","s2","你好","success").contents)

    Dict = []
    Dict.append(test.make_structlist("hello world","s2","你好","success"))
    print(test.make_structlist("hello world","s2","你好","success").contents)
    print("-->",Dict[0])
    print("--->",Dict[0].name)
