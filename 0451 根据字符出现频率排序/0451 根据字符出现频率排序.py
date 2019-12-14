#label: dictionary/heap difficulty: medium

class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        dic = Counter(s)
        
        res = ""
        dic = sorted(dic.items(), key = lambda x: x[1], reverse = True)
 
        for key, value in dic:
            res += value * key
            
        return res


