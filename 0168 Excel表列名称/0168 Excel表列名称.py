#label: maths difficulty: easy

"""
思路：

十进制转二十六进制。

比较特殊的地方在于没有从0开始，一般十进制是0~9， 二进制是0~1，这个二十六进制是1~26.

所以需要处理一下：

每次循环先把n - 1，这样可以变成0~25的范围。

"""

class Solution:
    def convertToTitle(self, n: int) -> str:
        #10进制转26进制
        res = ""
        while n:
            n -= 1
            char = chr(ord('A') + n % 26)
            n //= 26
            res += char
        return res[::-1]

