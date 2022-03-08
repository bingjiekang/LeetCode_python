#----1----56 ms	15 MB
"""将罗马数字转化成数字，通过模拟举例即可，将罗马数字对应的数字存放到对应字典中，由于从前往后，对应的罗马数字都是依次减少的，而特殊的罗马数字会是小的在大的前面，所以，从前往后读取若
这一位比后一位大，则加上这个罗马数字对应的数字，若这一位比后一位罗马数字小，则减去这一位罗马数字对应的数字即可。"""
class Solution:
    def romanToInt(self, s: str) -> int:
        Dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}  #模拟出罗马数字和对应的数字
        sult = 0      #用来存放转换后的数字
        length = len(s)     #记录字符的长度
        for i in range(length):  #从前往后依次读取字符下标
            if i == length-1:     #若为最后一个 则直接加上对应下标元素，对应的数字。
                sult+=Dict[s[i]]
            else:
                if Dict[s[i]]<Dict[s[i+1]]:   #若这一位的罗马数字比下一位小 则减去这一位罗马数字对应的数
                    sult-=Dict[s[i]]
                else:
                    sult+=Dict[s[i]]          #否则 则加上这一位罗马数字对应的数
        return sult
