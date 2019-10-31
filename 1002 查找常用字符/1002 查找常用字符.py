#label: array difficulty: easy

"""
第一种思路：

利用dict的键值对，先把每个字符的重复情况找出来放在dic里，然后遍历整个字符串，用min来取交集统计重复的字符。

"""

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        n = len(A)
        dic = [Counter(A[i]) for i in range(n)]
        compare = dic[0]
        
        for i in range(1, n):
            for key in compare:
                compare[key] = min(compare[key], dic[i][key])
                
        res = list()
        for key in compare:
            for i in range(compare[key]):
                res.append(key)
                
        return res


"""
第二种思路：

利用&运算符找重复的字母。

"""

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        compare = collections.Counter(A[0])  
        
        for i in A:
            compare &= collections.Counter(i)
                
        return list(compare.elements())

