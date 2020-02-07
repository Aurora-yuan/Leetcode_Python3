#label: array difficulty: medium

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for j in range(n)]
        
        i, j, di, dj = 0, 0, 0, 1
        for number in range(1, n ** 2 + 1):
            res[i][j] = number            
            if res[(i + di) % n][(j + dj) % n] != 0: #需要转向
                di, dj = dj, - di  #0 1 变 1 0, 1 0 变 0 -1, 0 -1 变 -1, 0, -1 0 变 0 1                 
            i += di
            j += dj
            
        return res


