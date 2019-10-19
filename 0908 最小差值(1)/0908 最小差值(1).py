#label: maths difficulty: easy

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        a = sorted(A)
        left = a[0] + K
        right = a[-1] - K
        if left >= right:
            return 0
        else:
            return right - left
