#----1-----3340 ms	15.4 MB
class Solution:
    def twoSum(self, target ,*nums):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]

   
#----2-----788 ms	15.4 MB
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(0,len(nums)):
#             temp = target-nums[i]
#             if temp in nums and nums.index(temp)!=i:
#                 return [i,nums.index(temp)]
#


def main():
    sm = Solution()
    print(sm.twoSum(7,1,2,3,3,5,6))





if __name__=="__main__":
    main()
                
