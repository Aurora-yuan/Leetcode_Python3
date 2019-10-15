#label: string difficulty: easy

"""
思路一：

直接调python库
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1
    
“”“
第二种思路：

把haystack可能为needle的子串全部找出来匹配一遍。

”“”

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for i, char in enumerate(haystack):
            if char == needle[0]:
                if haystack[i:i + len(needle)] == needle:
                    return i
                
        return -1


  
    
