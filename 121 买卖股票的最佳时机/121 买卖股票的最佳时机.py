#label: 动态规划 difficulty: easy
"""
第一种思路：

直白的麻瓜解法，线性扫描，如果右侧的最大元素减去当前元素的值大于目前的profit，就把profit刷新。

缺点很慢。

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for index in range(len(prices)-1):
            sub = max(prices[index+1:]) - prices[index]
            if sub > profit:
                profit = sub
        return profit

"""
第二种思路：

动态规划。

用一个变量minelement记录下左侧的最小值，

当扫描到第i个元素时，如果在这一天卖股票，盈利就是dp[i] = prices[i] - minelement

                                     如果在这一天不卖股票，盈利还是dp[i] = dp[i - 1]

所以 dp[i] = max(dp[i-1], prices[i] - minelement)

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0
        dp = [0]
        minelement = prices[0]
        for i in range(len(prices)):
            minelement = min(prices[i], minelement)
            dp.append(max(prices[i]-minelement,dp[i-1]))
            if dp[-1] > profit:
                profit = dp[-1]
        
        return profit
