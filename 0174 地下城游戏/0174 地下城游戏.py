# label: dynamic programming difficulty: hard

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # 官方题解
        m,n = len(dungeon),len(dungeon[0])
        BIG = 10 ** 9
        dp = [[BIG for _ in range(n+1)] for _ in range(m+1)]
        dp[m][n-1] = dp[m-1][n] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                minn = min(dp[i+1][j],dp[i][j+1])
                dp[i][j] = max(minn-dungeon[i][j],1)

        return dp[0][0]
