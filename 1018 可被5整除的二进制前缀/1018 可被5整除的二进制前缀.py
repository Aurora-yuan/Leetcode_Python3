#label: maths difficulty: easy

"""
思路：

不用专门将二进制转换为十进制，因为是从最短到最长遍历，每次将当前位置数*2+后一位置数即可求得十进制表示

"""

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        n = A[0]
        res = list()
        for i in range(0,len(A)-1):
            if n % 5 == 0:
                res.append(True)
            else:
                res.append(False)
            n = n * 2 + A[i+1]
        
        if n % 5 == 0:
            res.append(True)
        else:
            res.append(False)
        return res
