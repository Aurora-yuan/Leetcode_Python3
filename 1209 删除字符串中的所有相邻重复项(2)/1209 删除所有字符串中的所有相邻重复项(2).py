#label: string difficulty: medium

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #暴力法求解
        for i in range(len(s)):
            if i + k <= len(s) and s[i:i + k] == s[i] * k:
                return self.removeDuplicates(s[:i] + s[i + k:], k)
        return s


