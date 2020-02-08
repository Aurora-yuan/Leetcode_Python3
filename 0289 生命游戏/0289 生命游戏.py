#label: array difficulty: medium

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m,n = len(board),len(board[0])
        dx = [1,-1,0,0,1,1,-1,-1]
        dy = [0,0,1,-1,1,-1,1,-1]
        
        def countLiveCells(x0,y0):
            cnt = 0
            for i in range(8):
                x = x0 + dx[i]
                y = y0 + dy[i]
                if 0 <= x < m and 0 <= y < n and board[x][y] == 1:
                    cnt += 1
                    
            return cnt
        
        liveCellSet = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1 and countLiveCells(i,j) in [2,3]:
                    liveCellSet.add((i,j))
                elif board[i][j] == 0 and countLiveCells(i,j) == 3:
                    liveCellSet.add((i,j))
                    
        for i in range(m):
            for j in range(n):
                if (i,j) in liveCellSet:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
