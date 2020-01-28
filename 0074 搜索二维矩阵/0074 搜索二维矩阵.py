#label: 二分查找 difficulty: medium

"""

思路：

从左下角开始走，当前值比target大，就往上走；当前值比target小，就往右走；当前值=target就返回True。

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        
        x,y = m - 1, 0
        
        while 1:
            if x < 0 or x >=m or y < 0 or y >= n:
                return False
            val = matrix[x][y]
            if val  == target:
                return True
            elif val > target:
                x -= 1
            else:
                y += 1
                
        return False
    
