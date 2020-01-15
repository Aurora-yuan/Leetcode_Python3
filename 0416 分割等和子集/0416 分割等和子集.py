#label: dynamic programming difficulty: medium

"""
思路：

见https://blog.csdn.net/qq_17550379/article/details/82899422

"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        result = sum(nums)

        if result%2 != 0:
            return False
        # nums=sorted(nums,key=lambda x:-x)
        return self._canPartition(nums, len(nums) - 1, result//2)

    def _canPartition(self, nums, index, result):
        if result == 0:
            return True

        if result < 0 or index < 0 or nums[index] > result:
            return False
        
        return self._canPartition(nums, index - 1, result - nums[index]) or \
            self._canPartition(nums, index - 1, result)

