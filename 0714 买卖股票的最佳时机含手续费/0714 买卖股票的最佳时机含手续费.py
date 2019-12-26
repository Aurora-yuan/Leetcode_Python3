#label: dynamic programming difficulty: medium

"""
思路：

分析见https://blog.csdn.net/ggdhs/article/details/92380969

"""

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        for i, price in enumerate(prices):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = -price
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee) #获取利润的时候减去手续费
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])        
        return dp[len(prices)-1][0] if prices else 0


