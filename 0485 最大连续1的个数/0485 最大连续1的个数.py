#label: array difficulty: easy

"""
第一种思路：

直接暴力求解。

"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 0
        l = 0
        for i in nums:
            if i:
                l += 1
                res = max(l, res)
            else:                
                l = 0
        return res

"""
第二种思路：

动态规划，用dp[i]表示从0~ i 的最长连续1序列的长度，

显然dp[0] = nums[0]，

对于i！= 0 的情况，有

dp[i] = dp[i - 1] + 1 if nums[i] == 1  OR

dp[i] = 0 if nums[i] != 1

"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i]:
                dp.append(dp[i-1] + 1)
            else:
                dp.append(0)
        # print dp
        return max(dp)

