#----1-----32 ms	15.1 MB
"""若目标字符串在字符串中，可通过python中的index函数可以快速找到对应字符，找不到返回-1即可"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:   #如果目标字符串在字符串内 直接查找即可
            return haystack.index(needle)
        else:                    #不在则返回-1
            return -1
#----2-----52 ms	17.3 MB
"""记录目标字符串第一个字符和最后一个字符，查找字符串，若字符串中出现和目标字符串第一个字符或最后一个字符相同的字符，则分别放入列表中,通过记录目标字符串的长度，
判断若头字符在lt_begin出现，则判断对应尾字符是否在lt_end中出现，若出现则截取对应字符串判断和目标字符串是否相同，相同则返回头字符对应下标，若整个循环结束后未找到，
则返回-1，若查找为空返回0"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":   #查找目标字符串为空返回0
            return 0
        lt_begin = []    #存放出现和头字符相同的对应下标
        lt_end = []      #存放出现和尾字符相同的对应下标
        needle_begin = needle[0]   #记录目标字符串的头字符
        needle_end = needle[-1]    #记录目标字符串的尾字符
        length = len(haystack)     #记录字符串的长度
        length_needle = len(needle)   #记录目标字符串的长度
        for i in range(length):   
            if haystack[i]==needle_begin:  #若和字符串内的字符和头字符相同，将其下标加入到lt_begin
                lt_begin.append(i)
            if haystack[i]==needle_end:    #若和字符串内的字符和尾字符相同，将其下标加入到lt_end
                lt_end.append(i)
        for i in lt_begin:         
            temp = i+length_needle-1      #找到头字符下标对应的尾字符下标
            if temp in lt_end:            #若对应尾字符下标在lt_end中，则截取对应字符串若和对应目标字符串相同则返回，头字符下标
                temp = temp+1
                if haystack[i:temp] == needle:
                    return i
        return -1                 #若找不到则返回-1
