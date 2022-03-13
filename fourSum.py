#----1-----760 ms  15 MB
"""和三数之和相似，不同的是，这是四个数求和，结果得到和目标值相同的数的组成。通过固定最外层两个，然后通过控制内层两个，一个从前往后，一个从后往前，然后倒数第三层移动，最后倒数第一层在移动，
利用双指针得出答案"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()     #原列表排序
        length = len(nums)  #获取长度
        i = 0
        lt = []       #用来存储答案结果
        if length<4:   #当列表中数据小于四个时，直接返回空列表，不能构成答案所需目标
            return lt
        while i<length-3:   #最外层循环 即第一个数
            k = i+1
            while k<length-2:     #第二层循环 第二个数
                j = k+1            #第三层循环 第三个数
                end = length-1      #第四层循环 第四个数
                while j<end:      #双指针 控制第三第四个数，进行查找
                    nm = target + (-1)*(nums[i]+nums[j]+nums[k])    #获得满足目标target第四个数的具体数字
                    while nums[end]>nm and j<end:   #当不满足时 对第四层数进行往前推进
                        end-=1 
                    if (j<end and nums[end]==nm and [nums[i],nums[k],nums[j],nums[end]] not in lt):   #如果满足目标要求，且在答案列表中不存在则加入到答案列表中
                        lt.append([nums[i],nums[k],nums[j],nums[end]])
                    j+=1
                    while j<length-1 and nums[j]==nums[j-1]:        #用来去除第三层重复的数
                        j+=1    
                k+=1
                while (length-1)>k and nums[k]==nums[k-1]:          #用来去除第二层重复的数
                    k+=1
            i+=1
            while 0<i<length-3 and nums[i]==nums[i-1]:              #用来去除第一层重复的数
                i+=1
        return lt
