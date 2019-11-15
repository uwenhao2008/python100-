#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年11月11日 12:28 
tip-->兴趣是最好的老师<--
条件现所如下：
1.英国人住在红色的房子里
2.瑞典人养狗作为宠物
3.丹麦人喝茶
4.绿房子紧挨着白房子，在白房子左边
5.绿房子的主人喝咖啡
6.抽Pall Mall牌香烟的人养鸟
7.黄色房子里的人抽Dunhill牌香烟
8.住在中间那个房子里的人喝牛奶
9.挪威人住第一个房子里面
10.抽Blends牌香烟的人和养猫的人相邻
11.养马的人和抽Dunhill牌香烟的人相邻
12.抽BlueMaster牌香烟的人喝啤酒
13.德国人抽Prince牌香烟
14.挪威人和住在蓝房子的人相邻
15.抽Blend牌香烟的人和喝矿泉水的人相邻
# 基本模型的定义：
五种颜色的房子，五种国籍，五种饮料，五种宠物，五种香烟    类型+值二元组来描述
# 
# https://blog.csdn.net/weixin_45492196/article/details/100887150
上卖弄网站的解决方法貌似不需要这么多判断条件  分析分析~~~  因为他用了 itertools.permutations
"""
# from enum import Enum    # 引入枚举类
# 创建 给定条件 的数据结构
class StructItem():
    # 初始化常量
    GROUPS_ITEM, GROUPS_COUNT = 5, 5
    COLOR_BLUE,COLOR_RED,COLOR_GREEN,COLOR_YELLOW,COLOR_WHITE = 0,1,2,3,4
    NATION_NORWAY,NATION_DANMARK,NATION_SWEDEND,NATION_ENGLAND,NATION_GERMANY = 0,1,2,3,4
    DRINK_TEA, DRINK_WATER, DRINK_COFFEE, DRINK_BEER, DRINK_MILK = 0,1,2,3,4
    PET_HORSE, PET_CAT,PET_BIRD,PET_FISH,PET_DOG = 0,1,2,3,4
    CIGARET_BLENDS,CIGARET_DUNHILL,CIGARET_PRINCE,CIGARET_PALLMALL,CIGARET_BLUEMASTER = 0,1,2,3,4
    type_house,type_nation,type_drink,type_pet,type_cigaret = 0,1,2,3,4

    # # GROUP结构体
    # class ITEMTYPE():
    #     def __init__(self,type_house,type_nation,type_drink,type_pet,type_cigaret):
    #         self.type_house = type_house
    #         self.type_nation = type_nation
    #         self.type_drink = type_drink
    #         self.type_pet = type_pet
    #         self.type_cigaret = type_cigaret
    # def make_ITEMTYPE(self,type_house,type_nation,type_drink,type_pet,type_cigaret):
    #     return self.ITEMTYPE(type_house,type_nation,type_drink,type_pet,type_cigaret)

    valueNames = [[COLOR_BLUE,COLOR_RED,COLOR_GREEN,COLOR_YELLOW,COLOR_WHITE],[NATION_NORWAY,NATION_DANMARK,NATION_SWEDEND,NATION_ENGLAND,NATION_GERMANY],
    [DRINK_TEA, DRINK_WATER, DRINK_COFFEE, DRINK_BEER, DRINK_MILK],[PET_HORSE, PET_CAT,PET_BIRD,PET_FISH,PET_DOG],[CIGARET_BLENDS,CIGARET_DUNHILL,CIGARET_PRINCE,CIGARET_PALLMALL,CIGARET_BLUEMASTER]
    ]
    
    # 线索模型定义  线索1,2,3,5,6,7,12,13
    tagBinds = [[type_house,COLOR_RED,type_nation,NATION_ENGLAND],[type_nation,NATION_SWEDEND,type_pet,PET_DOG],
                [type_nation,NATION_DANMARK,type_drink,DRINK_TEA],[type_house,COLOR_GREEN,type_drink,DRINK_COFFEE],
                [type_cigaret,CIGARET_PALLMALL,type_pet,PET_BIRD],[type_house,COLOR_YELLOW,type_cigaret,CIGARET_DUNHILL],
                [type_cigaret,CIGARET_BLUEMASTER,type_drink,DRINK_BEER],[type_nation,NATION_GERMANY,type_cigaret,CIGARET_PRINCE]]
    # 线索 10，11，14，15
    # [type,value,relation_type,relation_val]
    relations = [[type_cigaret,CIGARET_BLENDS,type_pet,PET_CAT],[type_pet,PET_HORSE,type_cigaret,CIGARET_DUNHILL],
                [type_nation,NATION_NORWAY,type_house,COLOR_BLUE],[type_cigaret,CIGARET_BLENDS,type_drink,DRINK_WATER]]

    def __init__(self):    
        pass

    # 创建关系绑定类    线索 10，11，14，15
    class RELATION():
        def __init__(self,type,val,relation_type,relation_val):
            self.type = type
            self.val = val
            self.relation_type = relation_type
            self.relation_val = relation_val   
    def make_relation(self,type,val,relation_type,relation_val):
        return self.RELATION(type,val,relation_type,relation_val)

    # 创建线索关系  线索1,2,3,5,6,7,12,13
    class BIND():
        def __init__(self,first_type,first_val,second_type,second_val):
            self.first_type = first_type
            self.first_val = first_val
            self.second_type = second_type
            self.second_val = second_val  
    def make_bind(self,first_type,first_val,second_type,second_val):
        return self.BIND(first_type,first_val,second_type,second_val)

    class ITEM_TYPE():
        def __init__(self):
            self.type_house = 0
            self.type_nation = 0
            self.type_drink = 0
            self.type_pet = 0
            self.type_cigaret = 0
    def make_itemtype(self):
        return self.ITEM_TYPE()


    # 创建relation 结构体    终于搞出来了！！！
    def Struct_relation(self,relations):
        relations_list = []
        for i in range(len(relations)):
            type = relations[i][0]
            val = relations[i][1]
            relation_type = relations[i][2]
            relation_val = relations[i][3]
            # 下面这行，暗示了python中万物为对象的哲学
            relations_list.append(self.RELATION(type,val,relation_type,relation_val))
        return relations_list

    def Struct_bind(self,tagBinds):
        tagBinds_list = []
        for i in range(len(self.tagBinds)):
            first_type = self.tagBinds[i][0]
            first_val = self.tagBinds[i][1]
            second_type = self.tagBinds[i][2]
            second_val = self.tagBinds[i][3]
            tagBinds_list.append(self.BIND(first_type,first_val,second_type,second_val))
        return tagBinds_list

    # GROUP 为结构体 self.make_itemtype(type_house,type_nation,type_drink,type_pet,type_cigaret)
    # 得到group type类型的值  解决类似于 1号房子的颜色是什么 的问题
    def GetGroupItemValue(self,GROUP,type):
        return GROUP.type

    # 通过group数据type类型的val，找到对应的GroupId
    # 解决类似于 知道 绿房子的主人喝咖啡，判断这个方式是不是三号房  之类的问题
    def FindGroupIdxByItem(self,GROUP,type,value):
        for i in range(self.GROUPS_COUNT):
            if self.GetGroupItemValue(GROUP[i],type) == value:
                return i
        return False

    def ArrangePeopleDrinks(self,groups):
        pass


    # 这里之所以没有用 for循环0,1,2,3,4就是因为通过第一个房子住的挪威人进行了减枝操作的缘故，我这里的groupIdx 直接从1开始计数的，因为我传入的是1
    def EnumHouseNations(self,groups,groupIdx):
        if groupIdx == self.GROUPS_COUNT:
            self.ArrangePeopleDrinks(groups)
            return
        # 因为NATION_NORWAY 住0号房子，所以这里从0 开始，所以下面是range(5)
        for i in range(5):
            if not self.IsGroupItemValueUsed()

    # 9.挪威人住第一个房子里面
    def ArrangeHouseNations(self,groups):
        groups[0].type_nation = self.NATION_NORWAY
        # 第一个房子住NATION_NORWAY，从下一个继续开始遍历 人的国籍
        self.EnumHouseNations(groups,1)

    # 判断唯一性  遍历每个group的所有item_type,若是其在别已遍历的group里已经被使用，则返回True
    # 设计程序的时候，思维简单点，这里之所以让参数里有val就是为了 用它喝以前有的数据去比较的，若是没有了这里大的val那么程序实现起来会复杂一点
    def IsGroupItemValueUsed(self,groups, groupIdx, item_type, val):
        for i in range(groupIdx):
            if groups[i].item_type == val:
                return True
        return False

    def EnumHouseColors(self,groups,groupIdx):
        if groupIdx == self.GROUPS_COUNT:
            self.ArrangeHouseNations(groups)
            return
        # 因为条件4.绿房子紧挨着白房子，在白房子左边  所以只需要循环4次 因为最后一间房子肯定不是绿房子
        for i in range(4):
            if not self.IsGroupItemValueUsed(groups, groupIdx, self.type_house, i):
                groups[groupIdx].type_house = i 
                if i == self.COLOR_GREEN:
                    # 让绿房子的下一个是白房子，同时进行下一次遍历  这么操作可以利用判断条件进行剪枝操作
                    # 递归过程中 若是type_house为COLOR_GREEN，那么就让下一组房子的颜色 默认为COLOR_WHITE，并从系一组房子接着递归，若是又遇到了COLOR_GREEN，则groupIdx--，即返回上一层递归接着往后运行
                    groups[groupIdx+1].type_house = self.COLOR_WHITE
                self.EnumHouseColors(groups, groupIdx + 1)
                # 下面这部非常关键，若没有 -=  那么就不会进行深度优先了~~~~~~~~~~
                if i == self.COLOR_GREEN:
                    groupIdx -= 1





    def main(self):
        temp = self.make_itemtype()
        GROUP = []
        for i in range(self.GROUPS_COUNT):
            GROUP.append(temp)
        self.EnumHouseColors(GROUP,0)
        


gpitem = StructItem()
relations = gpitem.Struct_relation(gpitem.relations)
tagbinds = gpitem.Struct_bind(gpitem.tagBinds)
gpitem.main()




# [0 for _ in range(self.GROUPS_COUNT)]  快捷定义[0,0,0,0,0]


# 传入的是列表的话 添加*就可以依次转换为函数对应位置的参数了~~~~~~-------------------
# print(self.make_relation(*self.relations[0]).type)

# print(gpitem.Struct_relation(gpitem.relations)[0].type)



