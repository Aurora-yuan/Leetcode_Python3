#label: maths difficulty: easy

"""
1. 循环:
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
        
"""
2. 递归：终止条件：一直除到1为true，中间出现不能被3整除的数false :
"""

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n // 3)

"""
3.  如何完成进阶挑战？

考虑到注释里的 type n: int，而int类型中，最大的3的幂是3^{19} , 所以可以直接判断数n能否被3^{19}整除即可（当然，小于等于0的情况需要另外考虑）：
"""

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3**19 % n == 0

