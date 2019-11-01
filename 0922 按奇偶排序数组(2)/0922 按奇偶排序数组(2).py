#label: array difficulty: easy

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even,odd,res = list(),list(),list()
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        for j in range(len(A)):
            if j % 2 == 0:
                res.append(even.pop())
            else:
                res.append(odd.pop())
        return res
