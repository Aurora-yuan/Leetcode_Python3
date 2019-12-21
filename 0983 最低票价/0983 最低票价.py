#label: dynamic programming difficulty: medium

"""
思路：

dp[i]表示到第i 天的最低票价
不旅行就不买票，dp[i]=dp[i-1]
要旅行买票就分三种情况，日票、周票、月票，关键是从哪一天买

日票只能当天买
周票最划算的是一周前买
月票最划算的是一个月前买
比较三种情况得出最低票价，状态转移方程为：
dp[i] = min(dp[i-1]+日票价格， dp[i-7]+周票价格， dp[i-30]+月票价格）

"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1]+1
        dp = [0]*n
        for i in range(1, n):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1]+costs[0], dp[max(0,i-7)]+costs[1], dp[max(0,i-30)]+costs[2])
        return dp[-1]
