#label: dynamic programming difficulty: medium

"""
思路：

我们可以把数组 A 分成两部分来考虑：

前 T 个元素分成 K-1 个小组
剩余的元素分成 1 组，然后计算平均值之和的最大值
所以考虑采用动态规划，动态数组 dp 的转移方程应该是：

如果 k == 1，dp[i][k] = _sum[i] / i。代表着把前i个元素分成1段，平均值和的最大值就是自身的平均值
否则 dp[i][k] = max(dp[i][k], dp[j][k-1] + (A[j+1] + ... + A[i]) / (i-j))
为了便于计算数组中某一区间的和，我们额外建立一个 _sum 数组，用来保存数组 A 前 i 个元素之和

"""

class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        Asize = len(A)
        
        #dp[i][k]表示前i个数构成k个子数组时的最大平均值, 那么对于所有 0 <= j <= i-1
        #dp[i][k] = max(dp[i][k], dp[j][k-1] + (A[j+1] + ... + A[i]) / (i-j))
        dp = [[0] * (K + 1) for i in range(Asize + 1)]
        
        #_sum[i] = A[0] + ... + A[i - 1]
        _sum = [0 for i in range(Asize + 1)]
        for i in range(1, Asize + 1):
            _sum[i] = _sum[i - 1] + A[i - 1]
            dp[i][1] = _sum[i] / i
        
        for i in range(1, Asize + 1):
            for k in range(2, K + 1):
                for j in range(i):
                    dp[i][k] = max(dp[i][k], dp[j][k-1] + (_sum[i] - _sum[j]) / (i - j))
        
        return dp[Asize][K]
