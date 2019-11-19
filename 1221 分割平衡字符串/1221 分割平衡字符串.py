#label: 贪心算法 difficulty: easy

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num = 0
        res = 0
        for i in range(len(s)):
            if s[i] == 'L':
                num += 1
            else:
                num -= 1
            if num == 0:
                res += 1
                
        return res
