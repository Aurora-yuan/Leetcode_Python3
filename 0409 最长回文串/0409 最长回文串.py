#label: string difficulty: easy

class Solution:
    def longestPalindrome(self, s: str) -> int:
        res,flag = 0,0
        for char,freq in collections.Counter(s).items():
            if freq % 2 == 1:
                res += freq - 1
                flag = 1
            else:
                res += freq
                
        return res + flag
