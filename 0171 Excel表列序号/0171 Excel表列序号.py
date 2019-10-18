#label: maths difficulty: easy

class Solution:
    def titleToNumber(self, s: str) -> int:
        #相当于26进制转10进制
        l = len(s) - 1
        res = 0
        for index,item in enumerate(s):
            res += (ord(item)-ord('A')+1) * (26 ** (l - index))
        return res
