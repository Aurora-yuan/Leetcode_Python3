#label: 字符串 difficulty: easy
"""
思路：

先把题目描述里提到的func实现了吧，

然后通过对words里的每个元素都func一下得到新的数组record，

继续对queries里的每个元素也func一下得到一个数fq，剩下的工作就是在record里找有多少个数比fq大。

本来应该写二分的，比赛的时候怕写错，直接写了O（n)也可以过……
"""

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        record = []
        for word in words:
            record.append(self.func(word))
        record.sort()
        # print record
        
        n = len(record)
        res = []
        for q in queries:
            fq = self.func(q)
            cnt = 0
            for num in record:
                if num <= fq:
                    cnt += 1
                else:
                    break
            res.append(n - cnt)
        return res
    
    def func(self, word):
        for char in "abcdefghijklmnopqrstuvwxyz":
            t = word.count(char) 
            if t > 0:
                return t
        return 0

