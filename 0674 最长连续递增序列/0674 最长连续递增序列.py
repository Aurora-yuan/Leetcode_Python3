#label: array difficulty: easy

"""
思路：

求什么什么的连续序列，用DP。

dp[i]表示以nums[i]结尾的递增序列的长度。

状态转移方程很简单，

dp[0] = 0，

if dp[i] > dp[i - 1]， dp[i] = 1 + dp[i - 1]。这代表可以在前一个递增序列的基础上再延长一个数。

"""

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        
        res = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = 1 + dp[i - 1]
            res = max(dp[i], res)
                
        return res


