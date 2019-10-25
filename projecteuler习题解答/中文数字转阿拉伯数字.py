#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author:Wen
Time:2019年10月23日 16:15 
tip-->兴趣是最好的老师<--
例子：二十万 十是权位，万是节位
贰佰零陆万伍仟壹佰肆拾捌 = (2*100+6)*10000+5*1000+1*100+4*10+8
"""
class ChineseToNumb():
    # 定义汉字数字与阿拉伯数字的对应关系，以及相应的节权位
    chnDictNum = {'零':0,'壹':1,'贰':2,'叁':3,'肆':4,'伍':5,'陆':6,'柒':7,'捌':8,'玖':9}
    # 是否是节权位，以及对应的10的倍数
    chnUnitSection = {'拾':{'unitSection':0,'mul':1},
                      '佰':{'unitSection':0,'mul':10},
                      '仟':{'unitSection':0,'mul':100},
                      '万':{'unitSection':1,'mul':1000},
                      '亿':{'unitSection':1,'mul':10000000},
                      '万亿':{'unitSection':1,'mul':1000000000000}
                      }
    # 壹拾叁万零捌佰  遇到数字直接放入放入数组，遇到unitSection就处理前面的数字变为阿拉伯数字 (1*10+3)*1000+8*100
    # '壹佰肆拾伍万零陆拾叁'
    # 整体字符串转换为num，带权重的,先找权位，节字符串交给chineseToValue()处理
    def chnToNum(self,chnString):
        # 权位标记，同时用于判断chnString是否完结
        unitPos = 0
        numValue = 0
        tempString = ''
        while(unitPos <= len(chnString)):
            if unitPos == len(chnString):
                numValue = numValue + self.chineseToValue(tempString)
                return numValue
            # 判断当前 为 权位(不包括 拾，佰，仟)
            if chnString[unitPos] in self.chnUnitSection and self.chnUnitSection[chnString[unitPos]]['unitSection'] == 1:
                # 权位 为 万，亿，万亿  这里其实少了一个判断  万 与 万亿的区别！
                times = self.chnUnitSection[chnString[unitPos]]['mul']*10
                p = self.chineseToValue(tempString)
                numValue = numValue + p*times
                tempString = ''
            else:
                tempString = tempString + chnString[unitPos]
            unitPos = unitPos + 1

    # 节中的汉字数字转换为num   壹佰肆拾 = 1*100+4*10 
    def chineseToValue(self,chnString):
        tempNum = 0
        tempValue = ''
        for i in chnString:
            if self.isNum(i):
                # 应对chnString 为  一亿 和 陆仟伍佰零叁的尾数 这种特殊情况             
                if len(chnString)==1 or chnString[-1]==i:
                    tempNum = tempNum + self.chnDictNum[i] 
                else:
                    # 这里也需要权重，否则处理不了4500这种数据，会当作45处理
                    tempValue = tempValue + str(self.chnDictNum[i])
            else:
                tempNum = tempNum + int(tempValue)*self.chnUnitSection[i]['mul']*10
                tempValue = '' 
        return int(tempNum)

    # 判断是数字  还是权 数字返回True
    def isNum(self,chnString):
        if chnString in self.chnDictNum:
            return True
        else:
            return False

# strNum = '陆拾叁'
# strNum = '壹亿肆仟伍佰万陆仟伍佰捌拾柒'
strNum = '叁亿伍仟零壹拾肆万捌仟玖佰陆拾贰'
trs = ChineseToNumb()
print(trs.chnToNum(strNum))

