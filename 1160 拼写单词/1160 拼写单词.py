#label: maths difficulty: easy

lass Solution:
    def countCharacters(self, words: List[str], chars: str) -> int: 
        from collections import Counter
        dic2 = Counter(chars)
        res = 0
        for word in words:
            if self.helper(Counter(word), dic2):
                res += len(word)
        return res
    
    def helper(self, dic1, dic2):
        for key, val in dic1.items():
            if key not in dic2 or val > dic2[key]:
                return False
        return True

