#label: maths difficulty: easy

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #和0326 3的幂 方法一样
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
