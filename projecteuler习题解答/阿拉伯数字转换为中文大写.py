#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年10月21日 14:57 
tip-->兴趣是最好的老师<--
# 阿拉伯数字转换为中文大写 三条规则
1.以10000为小结，小结的末尾即使是0，也不使用‘零’
2.小节内两个非零数字中间用‘零’
3.当小节的千位是0时，若本小节的前一小节无其他数字则不使用‘零’，否则就使用‘零’
例子：以200001010200为例
"""
class NumToChinese():
    chnNumChar = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
    chnUnitSection = ['','万','亿','万亿']
    chnUnitChar = ['','十','百','千']

    # 将一个节的数字转换为中文数字，利用中文数字表chnNumChar转换，利用chnUnitChar得到数字权位，unitPos变量作权位索引
    def SectionToChinese(self,section:int):
            chnStr = []
            strIns = ''
            unitPos = 0
            zero = True

            while(section>0):
                v = section%10
                if(v==0):
                    if((section==0) or (1-zero)):
                        # zero作用是保证多个连续的0只补充一个 中文 ‘零’
                        zero = True
                        chnStr.insert(0,self.chnNumChar[v])
                else:
                    # 至少有一个数字不是
                    zero = False
                    # 此位对应的中文数字
                    strIns = self.chnNumChar[v]
                    # 中文数字带节里的权位
                    strIns += self.chnUnitChar[unitPos]
                    # 此位对应的中文权位
                    chnStr.insert(0,strIns)
                unitPos = unitPos + 1
                section = section//10
            return ''.join(chnStr)     

    # num = 0 需要特殊处理，直接返回'零'  完成各节 权位的处理
    def NumberToChinese(self, num:int):
        chnStr = []
        unitPos = 0
        needZero = False
        strIns = ''

        while(num > 0):
            section = num % 10000
            if(needZero):
                chnStr.insert(0, self.chnNumChar[0])
            sec = self.SectionToChinese(section)

        # 我这里的逻辑还是有点混乱，好好整理下思路，其实编程很锻炼数学思维的！但是数学又是我的弱项

            # 是否需要节权位？
            strIns += (sec + self.chnUnitSection[unitPos]) if (section != 0) else self.chnUnitSection[0]
            chnStr.insert(0,strIns)
            # 千位是？需要再下一个section补零   例如10054念为  壹万零伍拾肆
            needZero = (section<1000) and (section>0)
            num = num//10000
            unitPos = unitPos + 1
        return ''.join(chnStr)
        
    
# num = 200001010200
# change = NumToChinese()
# change.NumberToChinese(num,'')

# num = 401000010
num = 8014052
change = NumToChinese()
# print(change.SectionToChinese(num))
print(change.NumberToChinese(num))





