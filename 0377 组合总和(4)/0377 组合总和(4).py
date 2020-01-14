#label: dynamic programming difficulty: medium

"""
思路：

dp[i]表示nums有多少种组成 i 的组合。

dp[0] = 1， 即什么都不选

dp[i] = dp[i - nums[0]] + dp[i - nums[1]] + dp[i - nums[2]] + .... + dp[i - nums[-1]]

"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #dfs只能通过一半左右的case,递归地方法会重复计算很多次，所以可以用dp来储存之前的结果，节省计算的时间
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1    
        nums.sort() 
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
                
        return dp[target]


