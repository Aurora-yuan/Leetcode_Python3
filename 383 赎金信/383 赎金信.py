#label: string difficulty: easy

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = collections.Counter(ransomNote) #r为字典类型
        m = collections.Counter(magazine)
        
        for key in r:
            if m.get(key):
                if m[key] < r[key]:
                    return False
            else:
                return False
            
        return True
              
