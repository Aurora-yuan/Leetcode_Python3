#label: string difficulty: easy

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        return " ".join(word[::-1] for word in words) #str[::-1]表示开始：结束：步长
        
