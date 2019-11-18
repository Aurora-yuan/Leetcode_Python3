#label: 位运算 difficulty: easy

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        while num % 4 == 0:
            num = num // 4
        if num == 1:
            return True
        return False

