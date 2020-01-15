#label: dynamic programming difficulty: medium

"""
思路：

动态规划，特点是A[: i]的解可以由A[: i - 1]的解计算而得。

每当A[i - 1] - A[i - 2] == A[i] - A[i - 1]的时候，A[i -2] A[i - 1] A[i]会构成一个新的子等差数组，

而之前的每个以A[ i - 1]结尾的子等差数组长度都可以加一，变成一个新的子等差数组，

所以可以得到递推关系： dp [i] = 1 + dp[ i - 1]。

"""

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp = [0] * len(A)
        
        res = 0
        for i in range(2, len(A)):
            if A[i - 1] - A[i - 2] == A[i] - A[i - 1]:
                dp[i] = dp[i - 1] + 1
            res+= dp[i]
 
        return res


