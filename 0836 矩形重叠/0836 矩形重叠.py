#label: maths difficulty: easy

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        [A, B, C, D], [E, F, G, H] = rec1, rec2
        x, y = (min(C, G) - max(A, E)), (min(D, H) - max(B, F))
        return x > 0 and y > 0
