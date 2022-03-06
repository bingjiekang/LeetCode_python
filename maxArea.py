#----1-----	192 ms	25.4 MB
"""使用双指针，指针所指位置为木桶的边界，通过边界变化来找到能容纳的最多水的容积。左指针为min_length指向桶的左边界，右指针为max_length指向桶的右边界，最大容积为sult 
sult = min(height[min_length],height[max_length]) * (max_length-min_length) 。min(height[min_length],height[max_length])为左右桶边界的最短的边，
(max_length-min_length) 为两边界之间的距离，通过逐步缩小两边界之间的距离，获得能容纳的最大水的容积。detail：如果左边界min_length的高度小于、等于右边界max_length的高度，
将左边界min_length向右移动，如果右边界max_length的高度小于左边界min_length的高度，将右边界max_length向左移动，直到两边界重合或者左边界在右边界右边停止，记录最大的容量即可
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        sult = 0   #用来存储最大的容量
        max_length = len(height)-1  # 右边界
        min_length = 0       #左边界
        while min_length<max_length:   #循环 当左边界一直在右边界左边时 一直循环查找下一部 
            temp = min(height[min_length],height[max_length]) * (max_length-min_length)  #记录此时左右边界木桶的容量
            if temp>sult:   #如果当前木桶容量大于之前存储的最大容量
                sult = temp   #更新最大容量 
            if height[min_length]<=height[max_length]:  #左边界小于等于右边界时，左边界右移
                min_length+=1     
            else:             #右边界小于左边界时，右边界左移
                max_length-=1
        return sult
