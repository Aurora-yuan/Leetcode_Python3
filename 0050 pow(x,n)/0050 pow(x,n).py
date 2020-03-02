#label: math difficulty: medium

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 第一种思路： 直接套用公式
        # return x ** n

        # 第二种思路：数学原理
        i = abs(n)
        res = 1.0
        while i != 0:
            if i % 2:
                res *= x
            x *= x
            i /= 2
        return res if n > 0 else 1/res
