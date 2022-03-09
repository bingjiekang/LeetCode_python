#----1-----36 ms	15.1 MB
"""通过比较列表中所有字符的前缀部分，如果相同则记录下来，不同则返回结果"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = len(min(strs))  #记录列表中最小字符串的吃长度（即用来比较的最大范围）
        length = len(strs)           #获得列表中字符串的个数
        lt = []               # 用来存放公共重复字符
        for i in range(min_length):   #用来判断每位的字符
            temp_sum = 0         #用来辅助判断该字符是否是共有的
            temp_str = strs[0][i]   # 把第一个字符串的所有字符都作为标准 来判断其他的是否合理
            for j in range(length):    #举例出每个字符串
                if strs[j][i] == temp_str:  #若字符相同则计数
                    temp_sum +=1
            if temp_sum==length:     # 若计数与列表中字符串的个数相同，则证明这个字符是公共的
                lt.append(temp_str)
            else:            #不相同则直接返回
                break
        lt = "".join(lt)
        return lt
