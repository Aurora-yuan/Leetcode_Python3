#label: dynamic programming difficulty: medium

"""
思路：

选了所有的n，就不能选所有的n - 1和n + 1，

因此此题实际上是包装后的LeetCode-Python-198. 打家劫舍。

"""

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        values = [0 for _ in range(200001)]
        
        for i, num in enumerate(nums):
            values[num] += num
            
        # print values
        
        dp = [0 for _ in range(200001)]
        dp[0] = values[0]
        for i in range(1, len(values)):
            dp[i] = max(dp[i - 1], dp[i - 2] + values[i])
            
        return max(dp)

