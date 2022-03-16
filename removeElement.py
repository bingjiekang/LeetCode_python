#----1-----	40 ms	14.9 MB
"""暴力覆盖，从前往后查找，若出现需要删除的数，则通过另一个变量从该需要删除的数往后查找到与此目标数不同的数，覆盖前一个数，前一个数往后，后一个数继续查找若出现与目标数不同时，则继续覆盖
循环上述步骤直到后一个数查找到最后一位为止"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)     #用来获取范围
        for i in range(length):   #用来查找到第一个和目标数相同的数
            if nums[i]==val:   #查找到之后
                j = i+1        #用另一个变量获取位置，向后查找
                while(j<length):  #当范围在规定长度内 可以对该变量继续往后走
                    if nums[j]!=val:   #若该变量下标变量对应的数和目标数不同 则覆盖前一变量下标
                        nums[i] = nums[j]
                        i+=1       #继续遍历前一变量下标
                    j+=1 
                return i       #j查到最后 对应的下标i就是对应的长度
        return length       #查找不到对应的数，直接返回对应的长度即可

#----2-----	36 ms	14.9 MB
"""双指针：通过双指针，左指针向右，右指针向左，当左指针查找到和目标值相同时停下，当右指针查找到和目标值不同时停下，对左指针赋值右指针的值，对右指针进行左移操作，
当指针指向同一位置或者右指针在左指针左边时停止，返回右指针对应的值的下标，该下标加1即为对应答案"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)   
        left = 0        #左指针指向下标
        right = length-1  #右指针指向下标
        while(left<=right):   #当左指针在右指针左边时或者左指针和右指针相同，开始解答
            while(nums[left]!=val and left<right):   #查找到和目标值相同的地方停止
                left+=1
            while(nums[right]==val and left<=right):  #查找到和目标值不同的地方停止
                right-=1
            if left >= right:   #若左指针在右指针右边时，返回答案，解答结束
                return right+1
            nums[left] = nums[right]  #对左指针指向的和目标值相同的值覆盖和目标值不同的值
            right-=1    #对右指针进行左移
        
