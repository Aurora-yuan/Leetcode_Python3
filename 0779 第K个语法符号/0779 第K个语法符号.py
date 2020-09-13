# label: recursion difficulty: medium

"""
思路：

其他大佬总结的规律：
K在奇数位时，与N-1, (K+1)/2 位置的值相同
K在偶数位时，与N-1, K/2 位置的值相反

"""

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 0:
            return 0
        if K % 2:
            return self.kthGrammar(N-1, (K+1) / 2)
        else:
            return abs(self.kthGrammar(N-1, K / 2) - 1)

