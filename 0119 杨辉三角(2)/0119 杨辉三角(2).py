#label: array difficulty: easy

"""
思路：

对于杨辉三角中的第n行，第m个元素，它的值其实等于C（n-1）， （m-1）。

这好像是高中 二项式定理的内容，记不太清了。

所以直接套公式算就行了。

"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # C(n - 1，m - 1)
        n = rowIndex
        m = n + 1
        
        def Calculate(n, m):
            down = 1
            up = 1
            for i in range(1, m):
                down *= i
                
            for i in range(1, m):
                up *= (n + 1 -i)
                
            return up // down
            
        res = list()
        for i in range(1, m + 1):
            res.append(Calculate(n, i))
        
        
        return res


