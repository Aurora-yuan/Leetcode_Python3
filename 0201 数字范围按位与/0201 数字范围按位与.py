#label: 位运算 difficulty: medium


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 暴力模拟
        while n > m:
            n &= n - 1
        return n


