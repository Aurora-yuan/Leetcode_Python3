#label: 位运算 difficulty: easy

"""
第一种思路：

利用异或XOR来进行位运算。

"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for i in s:
            res ^= ord(i) - 97 #ord()将字符转换为十进制
        for i in t:
            res ^= ord(i) - 97
            
        return chr(res+97) #chr()将十进制转换为基础字符
  
“”“
第二种思路：

已知插入的一定是字母，所以可以遍历整个字母表+count函数来确定是哪一个字母。

”“”

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
    
        for char in alphabet:
            if s.count(char) != t.count(char):
                return char

“”“
第三种思路：

转成list之后求和，s和t的和之差就是相差的那个字母。

”“”

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(sum(ord(i) for i in list(t)) - sum(ord(j) for j in list(s)))

