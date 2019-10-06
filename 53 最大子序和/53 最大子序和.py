#label: 动态规划 difficulty: easy


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #dp[i]表示到第i个位置的最大连续子序列和
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        
        return max(dp)
