#----1-----40 ms	15.9 MB
"""由于是已经排好序的，可以利用二分法查找，查找到第一个和目标数相同的数的下标，若不存在，直接返回[-1,-1]。若存在，则往后找 找到第一个和目标数不同的数或者到列表末尾返回对应的结果下标-1即可"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0   #列表的左边界
        length = len(nums)-1    
        right = length   #列表的右边界
        if len(nums)==0 or target<nums[0] or target>nums[-1]:  #如果列表本身无数据 或 目标数比列表中最小的数还小 或 目标数比列表中最大的数还大 直接返回[-1,-1]即可
            return [-1,-1]
        while(left<=right):   #开始二分法查找
            mid = (left+right)//2   #中间的数
            if nums[mid]==target and left==right:   #如果中间值和目标值相同且left==right
                temp = mid    #用来获得最开始和目标值相同的值
                while temp<=length:  #用来获得最后一个和目标值相同的值
                    if nums[temp]!=target:
                        break
                    temp+=1
                if temp-1 > mid:  #如果不止一个和目标值相同，返回对应的前后下标
                    return [mid,temp-1]
                else:             #如果只有一个 返回mid即可
                    return[mid,mid]
            elif target<=nums[mid]:   # 如果目标数和中间数相同或者比中间数小 则想左查找（因为找到第一个和目标数相同的，所以和目标数相同也要向左找）
                if target == nums[mid]:    #如果target和nums[mid]相同 则下次查找的右边界为mid
                    right = mid
                else:                      #如果target小于nums[mid] 则下次查找的右边界为mid-1
                    right = mid-1  
            elif target>nums[mid]:    # 如果目标数比中间的数大 则向右查找
                left = mid+1
        return [-1,-1]  #找不到返回[-1,-1]
      
      
 #----2-----36 ms	16 MB
"""利用python函数，如果target在列表中，则找到第一个，再找最后一个即可，若不在列表中直接返回[-1,-1]
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:   # 列表中存在target
            Bg = nums.index(target)  #找到target的对应开始下标
            temp = Bg
            length = len(nums)     #获得列表的长度，即确定范围
            while temp<length:     #用来找最后一个和目标值相同的值
                if nums[temp]!=target: 
                    break
                temp+=1
            return [Bg,temp-1]    #返回对应的下标即可（由于从下标temp开始，则走过一次后，结果temp-1 最小的值和mid相同）
        else:
            return [-1,-1]        #不在列表中 返回[-1,-1]

