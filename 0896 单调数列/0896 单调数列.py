#label: array difficulty: easy

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return A == sorted(A) or A == sorted(A, reverse = True)
