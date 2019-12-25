#label: dynamic programming difficulty: medium

class Solution:
    def numTilings(self, N: int) -> int:
        # https://blog.csdn.net/weixin_30556161/article/details/101708435
        # https://blog.csdn.net/fuxuemingzhu/article/details/83059602
        dp = [[0] * 2 for _ in range(N + 1)]
        dp[0][0] = 1
        dp[1][0] = 1
        for i in range(2, N + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 2][0] + 2 * dp[i - 1][1]) % (10 ** 9 + 7)
            dp[i][1] = (dp[i - 2][0] + dp[i - 1][1]) % (10 ** 9 + 7)
        return dp[-1][0]


