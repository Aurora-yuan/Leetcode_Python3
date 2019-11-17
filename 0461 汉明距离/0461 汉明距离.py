#label: 位运算 difficulty: easy

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y # 两个十进制数按位异或
        n = bin(n) # 重新复制后的n是一个字符串
        
        return n.count('1')


