#label: dynamic programming difficulty: medium

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # 用dp[i][j] 表示 A[:i]和B[:j]的解
        # 因为是子数组，如果A[i]和B[j]不相等，dp[i][j]=0
        # 和最长子序列区别
        dp = [[0 for _ in range(len(B) + 1)] for i in range(len(A) + 1)]
        
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        return max([max(row) for row in dp])


