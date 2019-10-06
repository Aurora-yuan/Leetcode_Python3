#label: 动态规划 difficulty: easy
"""
问题的本质是求斐波那契数列（Fibonacci Sequence）

递推式为：dp[x] = dp[x - 1] + dp[x - 2]
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        #dp[i]表示到达第i阶台阶有多少种方式
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
