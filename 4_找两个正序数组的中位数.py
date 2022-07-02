#----1-----32 ms	15.1 MB
#寻找中位数：先合并两个数组，排序后判断数组内元素的个数，奇数则是中间的那一位，偶数为中间两位的平均数
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        length = len(nums1)
        if(length%2!=0):
            return nums1[length//2]
        else:
            return (nums1[length//2]+nums1[length//2-1])/2
