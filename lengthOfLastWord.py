#----1----32 ms	14.9 MB
"""通过split函数将字符串以空格隔开，输入到列表中，输出列表最后一个字符串的长度即可"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lt = [i for i in s.split()]   #将字符串s以空格隔开输入到列表中
        return len(lt[-1])    #输出最后一个列表的长度即可
