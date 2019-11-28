#label: string difficulty: easy

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        if len(A)!=len(B):
            return False
        for i in range(1, len(A)):
            tmp = A[i:] + A[:i]
            if tmp == B:
                return True
        return False

