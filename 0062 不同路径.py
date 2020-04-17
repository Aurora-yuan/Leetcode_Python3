# label: dynamic programming difficulty: easy

"""
思路：

动态规划。

dp[i][j] = dp[i-1][j] + dp[i][j-1]。注意边界条件。第一行或者第一列都只有一种走法。

"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*m]*n
        for i in range(n):
            for j in range(m):
                if not i and not j:
                    dp[i][j] = 1
                elif not i and j:
                    dp[i][j] = 1
                elif not j and i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1] 
