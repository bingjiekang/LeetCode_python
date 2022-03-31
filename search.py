#----1-----
"""二分法查找：从中间分开后，左右两边一定存在升序的序列。
若左边升序，则判断target是否在nums[left]到nums[mid]之间，若在他们之间则在左边范围内二分查找，否则就在右边二分查找
若右边升序，则判断target是否在nums[mid]到nums[right]之间，若在他们之间则在右边范围内二分查找，否则就在左边二分查找
最后找到nums[mid]==target,则返回下标，否则循环结束后，即找不到返回-1
判断是否是升序，可通过判断nums[0]和nums[mid]比较，若nums[0]小于nums[mid]则左边是升序的，否则右边是升序的"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1 
        while (left<=right):  
            mid = (left+right)//2
            if nums[mid]==target:   #如果nums[mid]==target 找到了 返回下标
                return mid
            elif nums[0]<=nums[mid]:   #左边是升序的
                if nums[left]<=target<nums[mid]:  #如果在左边 找左边
                    right = mid-1
                else:
                    left = mid+1    #否则找右边
            else:     #右边时升序的
                if nums[mid]<target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1   #找不到 返回-1
      
 #----2-----
"""如果target在里面 直接找到返回下标，不在返回-1"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1

