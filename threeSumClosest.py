#----1-----196 ms	14.9 MB
"""排序后，通过双指针，固定第一个下标为First_index的数后，通过移动第二个下标为Second_index的数和第三个下标为End_index的数，通过计算他们和目标数字的差距，重复记录，直到记录到和目标数字差距最小的数
当First_index+Second_index+End_index 的结果num小于目标target时，Second_index向后移动，num数增加，当num数大于目标target时，End_index向前移动"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()     #排序
        First_index = 0  #用来记录第一个下标 First_index
        length = len(nums)  
        sult = 10**5    #用来存放和目标target最接近的数
        while First_index<length-2:   #第一个下标的范围不能超过length-2个，超过则不会存在三个数满足接近target的要求
            Secont_index = First_index+1  #记录第二个下标   Second_index
            End_index = length-1      #记录最后一个下标  End_index
            while Secont_index<End_index:   #当第二个下标不超过第三个下标时，若超过则重复，可舍去（节省时间）
                num = nums[First_index]+nums[Secont_index]+nums[End_index]   #实际值num用来和目标值target进行比较
                if num>target:   #若实际值比目标值大 则第三个下标左移
                    End_index-=1
                elif num<target:   #若实际值比目标值小 则第二个下标右移
                    Secont_index+=1
                else:             #若相等 则放回该结果（没有比这更接近的数）
                    return num     
                if abs(target-num)<abs(target-sult):   #用来更新离目标值最近的数
                    sult = num    
            First_index+=1
        return sult
