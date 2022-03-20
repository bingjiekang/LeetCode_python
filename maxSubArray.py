#----1----184 ms	26.8 MB
"""动态规划，列表中连续的最大字符串可通过：从前到后，判断到从头到此下标内最大的连续子字符串，最后记录最大的即可。具体实施方法：到某个数据时，判断是从头到该数据之前的内的最大子字符串最大
还是加上这个数据后，对应的数据最大，将最大的加入，最后判断整个列表中最大的即可"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)   #获得列表的长度 
        dp = [nums[0]]    #对dp进行初始化
        for i in range(1,length):   #在范围内查找比较并记录
            dp.append(max(dp[i-1]+nums[i],nums[i]))   #加入到到目前为止最大的数
        return max(dp)
