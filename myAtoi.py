#----1-----
#注意：能转换成数字的只有类似"000123XXX","   123XXX","  +123XX","  -123XX"等
"""解决方案：将字符依次读取如果出现空格则跳过，继续读取下一个，如果出现+或-则记录符号并记录出现的次数，出现两次以上则返回0，且出现+或-后必须为数字0~9，否则返回0，整个字符串中可以无+或- 默认正。
如果出现数字0~9则开始转成对应数字，继续读取下一个字符，若出现一个不在0~9的字符时则结束程序返回这个结果。"""
class Solution:
    def myAtoi(self, s: str) -> int:
        js = 0  #用来记录字符串的下标
        length = len(s) #字符串的长度
        sult = 0   #转换的结果
        zf = 1    #转换结果的正负
        fz = 0    #+ -出现的次数
        max_len = 2**31   #限制范围  -2**31 ~ 2**31-1 
        while js<length: 
            if s[js]==" ":  #从前向后 出现空格则跳过 （在出现字符数字的前面）
                js+=1
                continue
            elif s[js]=="-" or s[js]=="+":  #出现+或- 记录正负 和出现的次数
                if (js+1)<length and ((ord(s[js+1])-48)<0 or (ord(s[js+1])-48)>9): #如果出现+或-后 其下一位若不是字符数字 则不能转换 返回0
                    return 0
                fz+=1      #记录+和-出现的次数
                if fz>1:    #出现两次及以上 返回0
                    return 0
                if s[js]=="-":  #若出现- 则记录为负数
                    zf = -1
                js+=1
                continue
            digst = ord(s[js])-48   #用来记录非空 和 非 (+或-)的字符
            while 0<=digst<=9 and sult<max_len:  #如果为字符数字且转换的结果仍在限制范围内 开始转换
                sult = sult*10+digst    #转换成数字
                js+=1
                if js<length:      #如果当前字符的下一个字符仍在字符串内
                    digst = ord(s[js])-48  #继续将字符转换成相对于0的数字
                else: 
                    break
            break      # 如果js超出范围或 读取的字符数字不在0~9内结束循环
        sult = zf*sult  #通过判断正负得到真正的结果 
        if sult<(-1)*max_len:   
            return (-1)*max_len  #不在范围限制内 返回边界数据
        elif sult>(max_len-1):
            return max_len-1
        else:           #在范围限制内 返回结果
            return sult
