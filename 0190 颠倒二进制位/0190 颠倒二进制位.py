#label: 位运算 difficulty: easy

"""
第一种思路：

直接模拟

"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)[2:] #转二进制
        b = "0" * (32 - len(b)) + b #补齐32位
        return int(b[::-1], 2) #转回十进制


"""
第二种思路：

利用位运算的性质，每次把n的最高位放到res的最低位，

然后左移res，右移n。

"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res <<= 1
            res += n & 1
            n >>= 1
        return res

