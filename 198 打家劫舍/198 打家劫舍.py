#label: 动态规划 difficulty: easy
"""
考虑前i项的结果dp[i]时，

当i = 1， 返回dp[0] = nums[0]

当i = 2， 返回dp[1] = max(nums[0], nums[1])

当i = 3， 分为偷3号房屋和不偷3号房屋，

               偷的情况下， 2号就不能偷了，结果为nums[2] + dp[0]

               不偷的情况下，结果为dp[1]

               所以返回dp[2] = max(dp[0] + nums[2], dp[1])

...

以此类推，dp[i] = max(dp[i-2] + nums[i], dp[i-1])
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [0 for _ in nums]  #dp[i]表示到第i家房屋能够偷窃到的最大金额
        dp[0] = nums[0]
       # dp[1] = max(dp[0], nums[1])
        
        for i in range(1,n):
            if i == 1:
                dp[i] = max(dp[0], nums[i])
            else:
                dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        
        return dp[-1]
