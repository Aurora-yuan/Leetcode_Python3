#label: dictionary difficulty: medium

"""
思路：

见 https://blog.csdn.net/qq_32424059/article/details/88698903

"""

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        map1 = dict()
        res = 0
        for a in A:
            for b in B:
                t = a + b
                map1[t] = map1.get(t, 0) + 1
                
        for c in C:
            for d in D:
                t = - c - d
                
                if t in map1:
                    res += map1[t]
                    
        return res


