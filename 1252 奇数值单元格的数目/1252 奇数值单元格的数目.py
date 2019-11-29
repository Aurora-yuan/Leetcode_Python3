#label: array difficulty: easy

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        b = [[0 for _ in range(m)] for _ in range(n)]
        for row,col in indices:
            for i in range(m):
                b[row][i] += 1
            for i in range(n):
                b[i][col] += 1
                
        res = 0
        for i in range(n):
            for j in range(m):
                if b[i][j] % 2 == 1:
                    res += 1
                    
        return res
