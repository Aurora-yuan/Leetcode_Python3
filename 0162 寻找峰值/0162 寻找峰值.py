#label: 二分查找 difficulty: medium

"""
第一种思路：

给定条件nums[i] ≠ nums[i+1]，直接找最大值的下标即可。

"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return nums.index(max(nums))

"""
第二种思路：

给定条件：nums[-1] = nums[n] = -∞，所以从i=0开始遍历数组元素nums[i],遇到的第一个nums[i] > nums[i+1]就是第一个峰顶，

比如[2,3,2,9,8],第一个满足条件的i是1，对应元素是3，正是峰顶。

这种思路的正确性在于在遇到第一个nums[i] > nums[i+1]之前，数组保持递增（题目条件约束保证了不会出现连续两个相等的元素），

所以当第一个nums[i] > nums[i+1]的时候，num[i]是上升和下降的分界线，即为峰顶。

"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        for index,item in enumerate(nums):
            if index + 1 < len(nums) and item > nums[index+1]:
                return index
            
        return len(nums) - 1
        
"""
第三种思路：

在第二种思路的基础上，运用二分查找的思想，

每次判断mid是不是峰顶，如果不是，则往较大的那一侧继续搜索。
 
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
          
        if len(nums) <= 1:
            return 0
        lo, hi = 0, len(nums) - 1
        while(lo < hi):
            # print lo,hi
            mid = lo + (hi - lo) / 2
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid - 1
                
        return lo


