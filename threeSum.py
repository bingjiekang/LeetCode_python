#----1-----4396 ms	17.8 MB
"""双指针，先对原数组进行升序排序，先固定一个下标i，然后将第二个数从i往后走，将end从后往前走，由于i固定后，随着j往后走，下标j对应的数字越来越大，则end下标对应饿数字越来越小，所以j往后走，end往前走"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()        #排序
        length = len(nums)   
        i = 0
        lt = [] 
        if length==0:     #为空则直接返回
            return lt
        while i<length and nums[i]<=0:   #下标i向后走，不超过数组的长度
            j = i+1     #下标j从i往后走  
            end = length-1   #下标end向前走
            while j<end: 
                nm = (-1)*(nums[i]+nums[j])   #得到固定i，j后，需要得到的数，
                while nums[end]>nm and j<end:  #将得到的数和从后行前走的下标为end的数进行比较
                    end-=1
                if (j<end and nums[end]==nm and [nums[i],nums[j],nums[end]] not in lt):  #如果i,j,end下标对应的数和为0 则判断该数组是否重复 不重复则加入结果中
                    lt.append([nums[i],nums[j],nums[end]])
                j+=1
            i+=1
        return lt
      
 #----2-----2696 ms	17.8 MB
#相比上个方法，去除了一些重复的数，减少了一些时间
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        i = 0
        lt = []
        if length==0:
            return lt
        while i<length and nums[i]<=0:
            j = i+1
            end = length-1
            while j<end: 
                nm = (-1)*(nums[i]+nums[j])
                while nums[end]>nm and j<end:   
                    end-=1
                if (j<end and nums[end]==nm and [nums[i],nums[j],nums[end]] not in lt):
                    lt.append([nums[i],nums[j],nums[end]])
                j+=1 
                while j<length-1 and nums[j]==nums[j-1]:  #用来去掉i第一个数重复的记录
                    j+=1    
            i+=1
            while (length-1)>i>0 and nums[i]==nums[i-1]:  #用来去掉j第二个数重复的记录
                i+=1
        return lt
