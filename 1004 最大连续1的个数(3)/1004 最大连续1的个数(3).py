#label: slide window/two pointers difficulty: medium

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l, res = 0, 0
        stack = []
        for r in range(len(A)):
            if A[r] == 0:
                stack.append(r)
            if len(stack)>K:
                l = stack.pop(0)+1
            else:
                res = max(res, r-l+1)
                
        return res 
