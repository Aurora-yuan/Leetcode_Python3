#label: maths difficulty: easy

"""
思路一：

最容易想到的方法。用字符串处理的方法，每个位取反。
"""

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        b = bin(N)[2:]  #为了去掉二进制前面的0b
        
        res = ""
        for char in b:
            if char == "0":
                res += "1"
            else:
                res += "0"
                
        return int(res, 2)

“”“
思路二：

非常巧妙，trick。对于一个正整数， 比如5 （101）， 其反码就是其所有二进制位上为1的数（111）减去这个正整数 = 111 - 101 = 010 （2）。
”“”

class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        M = 1
        while(M < N):            
            M = M << 1
            M += 1
 
        return M - N

