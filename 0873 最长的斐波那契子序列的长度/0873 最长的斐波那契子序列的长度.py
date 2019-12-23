#label: dynamic programming difficulty: medium

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n=len(A)
        tmp=set(A)
        res=0
        for i in range(n):
            for j in range(i+1,n):
                left=A[j]
                right=A[i]+A[j]
                length=2
                while right in tmp:
                    length+=1
                    left,right=right,left+right
                res=max(res,length)
        if res<3:
            return 0
        return res
                    


