#label: string difficulty: easy

"""
第一种思路：

暴力法，先统计A的词频再统计B的词频，最后按题意返回。

"""

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a = dict()
        b = dict()
        A = A.split(" ")
        B = B.split(" ")
        for item in A:
            if a.get(item, 0):
                a[item] += 1
            else:
                a[item] = 1
                
        for item in B:
            if b.get(item, 0):
                b[item] += 1
            else:
                b[item] = 1
        
        # print a, b
        res = list()
        for key in a:
            if a[key] == 1 and b.get(key, 0) == 0:
                res.append(key)
                
        for key in b:
            if b[key] == 1 and a.get(key, 0) == 0:
                res.append(key)
                
        return res

"""
第二种思路：

学习自讨论区: 拼接字符串A+B，然后返回拼接后的字符串中只出现过一次的单词

"""

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A + " " + B
        a = dict()
        A = A.split(" ")
        
        for item in A:
            if a.get(item, 0):
                a[item] += 1
            else:
                a[item] = 1
                
        res = list()
        for key in a:
            if a[key] == 1:
                res.append(key)
 
        return res

"""
第三种思路：

调库。

"""

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import defaultdict
        count = defaultdict(int)
        for word in A.split():
            count[word] += 1
        for word in B.split():
            count[word] += 1
     
        return [word for word in count if count[word] == 1]


