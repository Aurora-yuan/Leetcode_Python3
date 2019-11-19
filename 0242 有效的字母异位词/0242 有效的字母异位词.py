#label: sorted difficulty: easy

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmaps, hashmapt = dict(), dict()
        for char in s:
            hashmaps[char] = hashmaps.get(char, 0) + 1
        
        for char in t:
            hashmapt[char] = hashmapt.get(char, 0) + 1
            
        return hashmaps == hashmapt


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        return Counter(s) == Counter(t)

