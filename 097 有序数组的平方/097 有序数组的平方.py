#label: 双指针 difficulty: easy

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        return sorted([_ ** 2 for _ in A])
