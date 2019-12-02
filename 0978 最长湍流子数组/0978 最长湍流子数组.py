#label: slide window difficulty: medium

class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        ans = 1
        anchor = 0

        for i in xrange(1, N):
            c = cmp(A[i-1], A[i])  #python3中cmp用operator.eq替代
            if i == N-1 or c * cmp(A[i], A[i+1]) != -1:
                if c != 0: 
                    ans = max(ans, i - anchor + 1)
                anchor = i
        return ans
