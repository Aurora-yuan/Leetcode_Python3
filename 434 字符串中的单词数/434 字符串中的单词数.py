#label: string difficulty: easy

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())#分割包括空格，换行，制表位等，标点符号与单词一起，不影响
