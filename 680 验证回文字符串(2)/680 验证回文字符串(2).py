#label: 双指针 difficulty: easy

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n-1
        while left < right:
            if s[left]!=s[right]:
                return self.comp(s,left+1,right) or self.comp(s,left,right-1)
            else:
                left += 1
                right -= 1
        return True
    
    def comp(self,s,left,right):
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
