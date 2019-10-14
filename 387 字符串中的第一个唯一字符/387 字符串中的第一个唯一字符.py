#label: string difficulty: easy

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = collections.Counter(s)
        for i in range(len(s)):
            if dic[s[i]] < 2:
                return i
            
        return -1
