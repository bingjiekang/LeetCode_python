#----1-----36 ms	14.9 MB
"""通过对列表最后一个元素加1，然后再倒序从后先前判断，若数据大于9则向前进位1，一直判断到第二位，最后单独判断第一位，若大于9则向前加一位1，不大于9则直接返回"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]+=1   #列表最后一个数据加1
        temp = len(digits)-1    #得到列表的长度
        for i in range(temp,0,-1):   #倒序判断每个数据是否大于9
            if digits[i]>9:
                digits[i]%=10    #数据大于9 则进位，保存模10后的余数
                digits[i-1]+=1
        if digits[0]>9:    #单读判断第一位，若满足进位，则对列表进行扩充，否则直接返回即可
            digits[0]%=10
            digits = [1]+digits
        return digits   #返回答案
