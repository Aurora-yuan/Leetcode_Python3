#label: dynamic programming difficulty: medium

"""
思路：

类似LeetCode-Python-122. 买卖股票的最佳时机 II，区别在于前天买的今天才能卖，昨天买的今天不能卖。

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        for i, price in enumerate(prices):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = -price
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]) 
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i]) #前天买的今天才能卖
        return dp[i][0] if prices else 0


