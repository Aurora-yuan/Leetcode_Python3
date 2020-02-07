#label: array difficulty: medium

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        r,i,j = list(),0,0
        #di,dj控制前进的方向
        di,dj = 0,1
        
        for _ in range(m * n):
            r.append(matrix[i][j])
            matrix[i][j] = None
            if matrix[(i+di)%m][(j+dj)%n] == None: #来过了该转向了
                di,dj = dj,-di
                
            i+= di
            j += dj
            
        return r
