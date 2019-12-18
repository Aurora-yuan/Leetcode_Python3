#label: math difficulty: medium

"""
思路：

上公式，G(i) = i ^ (i / 2)。

"""

class Solution:
    def grayCode(self, n: int) -> List[int]:
        # G(i) = i ^ (i /2)
        dp = [0 for _  in range(2 ** n)]
        for i in range(1, 2 ** n):
            dp[i] = i ^ (i // 2)
        return dp


