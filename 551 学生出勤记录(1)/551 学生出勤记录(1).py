#label: string difficulty: easy

class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') > 1 or "LLL" in s:
            return False
        
        return True
