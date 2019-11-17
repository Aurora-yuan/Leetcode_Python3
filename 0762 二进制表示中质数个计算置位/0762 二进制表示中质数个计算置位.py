#label: 位运算 difficulty: easy

"""
思路：

输入限制在100，000的范围内，而2的20次方为1048576，所以只需要考虑20以内的质数。

"""

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        prime = set([ 2, 3, 5, 7, 11, 13, 17, 19])
        res = 0
        for i in range(L, R + 1):
            if bin(i).count("1") in prime:
                res += 1
        return res

