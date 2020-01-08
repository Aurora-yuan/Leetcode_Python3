#label: dynamic programming difficulty: easy

"""
第一种思路：

不限制买卖次数，要求算最大利润，

根据贪心的思想：那么能赚钱就买卖啊，

举例：对于输入[7,1,5,3,6,4]， 已经提前知道了所有第 i 天，股票的价格 price[i] ，

那么先持有7，发现第二天价格会跌，就卖掉手上的价格为7的股票，转而等到第二天买价格为1的股票，

到第三天，发现价格涨了，可以赚四块钱，果断卖掉盈利，同时买入当天的价格为5的股票，

发现第四天价格又跌到了3，于是把价格为5的股票抛出，转而等到第四天买入价格为3的股票，

第五天，能赚三块，卖掉盈利，然后持有价格为6的股票 ，

发现第六天价格降到4，于是把六块股票卖了，第六天买四块的股票。

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        res = 0
        min_price = prices[0]
        for i, price in enumerate(prices):
            if i == 0:
                continue
            else:
                if price > min_price: #能赚钱就赚
                    res += price - min_price
                min_price = price #会亏钱就不亏
            # print price, min_price, res
        return res

"""
第二种思路：

动态规划。

dp[i][k][0/1]表示第i天交易次数还剩k手上拿着1或者没拿0股票的状态
比如：
dp[2][1][1]表示第二天，还可以交易一次，手上持有股票
dp[3][5][0]表示第三天，还可以交易五次，手上没拿股票
求dp[len(prices) - 1][0][0]
 
dp[i][k][0] = max(dp[i – 1][k][0], dp[I – 1][k][1] + prices[i])
dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
第一题 k = 1
 
dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
dp[i][1] = max(dp[i - 1][1], 0 - prices[i])
 
当i = 0时，
dp[0][0] = 0
dp[0][1] = -prices[0]
第二题 k = infinity
所以k = k - 1
dp[i][0] = max(dp[i – 1][0], dp[I – 1][1] + prices[i])
dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        
        for i,price in enumerate(prices):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -price
                
            else:
                dp[i][0] = max(dp[i-1][0],dp[i-1][1]+price)
                dp[i][1] = max(dp[i-1][1],dp[i-1][0]-price)
                
        return dp[len(prices)-1][0] if prices else 0

