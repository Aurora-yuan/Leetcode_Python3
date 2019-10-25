#label: maths difficulty: easy

"""
思路一：

转换为字符串

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
        
“”“
思路二：

手动计算翻转之后的数字：

”“”

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xx = x
        if x < 0:
            return False
 
        reverse = 0
        while x > 0:
            x, tmp = divmod(x, 10)
            reverse = reverse * 10 + tmp
 
        return reverse == xx

