#label: 位运算 difficulty: easy

"""
思路：

记录一下前一位，每次跟前一位比较就好了。

"""

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        n, flag = divmod(n, 2)
        while(n):
            n, t = divmod(n, 2)
            
            if t == flag:
                return False            
            flag = t
            
        return True

