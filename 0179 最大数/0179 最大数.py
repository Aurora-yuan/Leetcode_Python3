#label: sort difficulty: medium

"""
思路：

自定义排序，让组合起来更大的排在前面。

"""


class Solution(object):
    def sort(self, x, y):
        return 1 if x + y < y + x else -1
    
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums or sum(nums) == 0:
            return "0" 
        nums = [str(i) for i in nums]
        nums.sort(self.sort)
        return "".join(nums)

