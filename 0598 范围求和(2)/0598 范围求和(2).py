#label: maths difficulty: easy

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        #直接找ops里两个方向上的最小值就好了,返回它们的乘积
        min1,min2 = m,n
        for op in ops:
            min1 = min(min1,op[0])
            min2 = min(min2,op[1])
            
        return min1 * min2
                
