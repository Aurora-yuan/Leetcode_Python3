#label:分治算法 difficulty:easy
"""
水题，按照题目要求，把数组排序后中间那个数就是众数。
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
  
        nums.sort()
        return nums[int(len(nums)/2)]

