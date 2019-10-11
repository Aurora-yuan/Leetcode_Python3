#label: string difficulty: easy

class Solution:
    def rotatedDigits(self, N: int) -> int:
        ans = 0
        for n in range(1,N+1):
            nset = set(map(int,str(n)))
            if any(x in nset for x in (2,5,6,9)):
                if not any(x in nset for x in (3,4,7)):
                    ans += 1
        return ans
