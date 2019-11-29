#label: dictionary difficulty: easy

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        
        dic = Counter(arr)
        
        s = set()
        for key,val in dic.items():
            if val in s:
                return False
            s.add(val)
            
        return True
