"""
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。
来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""理解
1.我们希望下一个数 比当前数大，这样才满足 “下一个排列” 的定义。因此只需要 将后面的「大数」与前面的「小数」交换，就能得到一个更大的数
2.我们还希望下一个数 增加的幅度尽可能的小，这样才满足“下一个排列与当前排列紧邻“的要求。为了满足这个要求，我们需要：
    1)在尽可能靠右的低位,进行交换，需要从后向前查找
    2)将一个尽可能小的「大数」与前面的「小数」交换。
    3)将「大数」换到前面后，需要将「大数」后面的所有数 重置为升序，升序排列就是最小的排列。
"""

#代码:
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length1 = len(nums)-1
        # 找出较小的数（从右往左）即nums[i]<nums[i+1]时的i
        while nums[length1-1]>=nums[length1] and length1>0:
            length1-=1
        tempmin = length1-1
        # 找出较大的数（从右往左）比较小的数大的数，此时较小数右边已经都是降序排列（因为上面已经走过，升序排列的就会停下）
        length2 = len(nums)-1
        while tempmin<length2 and nums[tempmin]>=nums[length2] and tempmin>=0:
            length2-=1
        tempmax = length2
        # 调换较小数和较大数的数据，即为顺序数的下一个数
        nums[tempmin],nums[tempmax] = nums[tempmax],nums[tempmin]
        # 确定左右对换的边界
        left = tempmin+1
        right = len(nums)-1
        # 已确定降序的数组，对换数据，变为升序。
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1

# def main():
#     temp = Solution()
#     lt = [1,4,2,2,7,1]
#     temp.nextPermutation(lt)
#     print(lt)


# if __name__ =="__main__":
#     main()


