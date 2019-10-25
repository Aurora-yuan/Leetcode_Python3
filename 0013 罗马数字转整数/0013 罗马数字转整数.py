#label: maths difficulty: easy

"""
第一种思路：

暴力解，能过但是有点慢。
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I": 1, "V":5, "X": 10, "L":50, "C":100, "D": 500, "M": 1000}
        stack = []
        res = 0
        for inx, item in enumerate(s):
            res += dic[item]
            # print res
            # s.append(item)
            if item == "V" or item == "X":
                if stack and stack[-1] == "I":
                    res -= 2
            elif item == "L" or item == "C":
                if stack and stack[-1] == "X":
                    res -= 20
            elif item == "D" or item == "M":
                if stack and stack[-1] == "C":
                    res -= 200
            stack.append(item)
        return res

"""
第二种思路：

来自答案区。

利用题意里的：通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例。

"""

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        a = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)):
            if i < len(s) - 1 and a[s[i]]<a[s[i+1]]:
                res -= a[s[i]]
            else:
                res += a[s[i]]
        return res
                
