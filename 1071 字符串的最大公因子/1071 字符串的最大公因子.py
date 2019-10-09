#label: string difficulty: easy

"""
思路：

题目需要求同时满足两个条件的字符串，那就把分别满足一个条件的字符串找出来，

然后取交集，返回长度最长的那个即可。
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1,l2 = len(str1), len(str2)
        set1, set2 = set(), set()
        for i in range(l1+1):
            if self.find(str1, str1[:i]):  #字符串切片截取不包括i
                set1.add(str1[:i])
                
        for i in range(l2+1):
            if self.find(str2, str2[:i]):
                set2.add(str2[:i])                
                
        res = list(set1 & set2)
        res = sorted(res, key = lambda x:-len(x))
        return res[0] if res else ""
        
    def find(self, string, tmp):  #tmp是否能除尽string
        string = string.replace(tmp, "")
        return len(string) == 0

