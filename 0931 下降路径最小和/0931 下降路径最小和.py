#label: dynamic programming difficulty: medium

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        m = len(A)
        n = m
        
        if A == [[]]:
            return 0
        
        dp = [[0 for _ in range(n)] for t in range(m)]
        for i in range(n):
            dp[0][i] = A[0][i]
            
        for i in range(1, m):
            for j in range(n):
                if not j: # the first column 
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + A[i][j]
                elif j == n - 1: # the last column
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + A[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1]) + A[i][j]
        return min(dp[-1])
                    


