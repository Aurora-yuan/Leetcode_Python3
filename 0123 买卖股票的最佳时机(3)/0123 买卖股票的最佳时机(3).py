#label: dynamic programming difficulty: difficult

"""
思路：

动态规划

dp[i][k][0/1]表示第i天交易次数还剩k手上拿着1或者没拿0股票的状态
比如：
dp[2][1][1]表示第二天，还可以交易一次，手上持有股票
dp[3][5][0]表示第三天，还可以交易五次，手上没拿股票
求dp[len(prices) - 1][0][0]
 
dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][k][0/1]表示第i天交易次数还剩k手上拿着1或者没拿0股票的状态
        max_k = 2
        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(max_k + 1)] for _ in range(n)]
        
        for i, price in enumerate(prices):
            for k in range(max_k, 0, -1):
                if i == 0:
                    dp[0][k][0] = 0
                    dp[0][k][1] = -price
                else:
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
                
        return dp[n - 1][max_k][0] if prices else 0

