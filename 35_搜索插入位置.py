#----1-----36 ms	15.6 MB
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        temp = len(nums)
        for i in range(temp):
            if target<=nums[i]:
                return i
        else:
            return temp
