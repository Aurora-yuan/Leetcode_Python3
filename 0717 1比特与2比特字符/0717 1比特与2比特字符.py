#label: array difficulty: easy

"""
思路：

遇到 1 索引+2，flag为False；遇到 0 索引+1，flag为True，最后返回flag即可。

"""

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-1] == 1:
            return False
        i = 0
        flag = True
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                flag = False
            else:
                i += 1
                flag = True
        return flag
