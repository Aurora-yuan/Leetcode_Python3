#label: array difficulty: easy

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even, odd,res = list(),list(),list()
        for i in A:
            if i % 2 ==0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd  #列表可以用+进行连接，和字符串一样
            
