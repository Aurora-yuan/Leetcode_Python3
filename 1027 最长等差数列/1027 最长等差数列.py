#label: dynamic programming difficulty: medium

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        #dp[i][d]表示以下标i结尾，公差为d的子序列的长度
        res = 1
        l = len(A)
        dp = [[1] * 20001 for j in range(l)]
        for i in range(1, len(A)):
            for j in range(i - 1, -1, -1):
                d = A[i] - A[j]
                d += 10001
                dp[i][d] = max(dp[i][d], dp[j][d] + 1)
                res = max(res, dp[i][d])
    
        return res


