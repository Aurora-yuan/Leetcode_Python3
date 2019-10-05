# label: 动态规划 difficulty: easy
"""
dp[0], dp[1]可以照抄cost[0]， cost[1]， 其他的 dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]，
最后可能从倒数第一个台阶走，也可能从倒数第二个台阶走，所以要判断一下怎么走更小

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        dp = [0 for _ in range(l+1)]  #创建一个有l个元素的列表且列表中的所有元素均为1
        dp[0],dp[1] = cost[0],cost[1]
        
        for i in range(2,l):
            dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
            
        return min(dp[l-1],dp[l-2])
