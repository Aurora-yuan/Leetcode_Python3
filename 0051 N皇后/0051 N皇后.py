#label: 贪心算法 difficulty: hard 

"""
思路：

一道经典的回溯题，十年前就学过了，现在才真的能写出来……惭愧惭愧

核心思想就是回溯，尝试每一种可能的下法，如果不满足条件，就倒退回上一次的状态。

判断皇后冲突时，

1. 横向冲突就是Y相同，X不同的位置上出现了别的Q

2. 竖向冲突就是X相同，Y不同的位置上出现了别的Q

3. /向冲突就是 X + Y的和 相同的坐标上出现了别的Q

4. \向冲突就是 Y - X的差 相同的坐标上出现了别的Q

"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["." * n for _ in range(n)]
 
        res = []
        def checkRowAndCol(row, col):
            for i in range(n):
                if (board[row][i] == "Q" and i != col) or (board[i][col] == "Q" and i != row): #发生了横向或者纵向冲突
                    return False
            return True
        
        def checkDoubleDio(row, col):
            add = row + col
            sub = col - row
            
            for x in range(n):
                if x == row: #跳过自身这个点
                    continue
                y = add - x
                # print add,sub, x, y
                if y >= 0 and y < n and x >= 0 and x < n and board[x][y] == "Q": #发生/冲突
                    return False
            
                y = sub + x
                if y >= 0 and y < n and x >= 0 and x < n and board[x][y] == "Q": #发生\冲突
                    return False
                
            return True
        
        
        def dfs(row, col):
            if col >= n: #本行所有位置都找完了
                return
            board[row] = "." * col + "Q" + (n - col - 1) * "." #把皇后放在(row, col)的位置上
            # board[row][col] = 'Q'
            if checkRowAndCol(row, col) and checkDoubleDio(row, col): #如果没有发生冲突
                if row == n - 1: #如果放下的是最后一个皇后
                    # print board
                    res.append(board[:]) #找到一个可行解啦！！！
                else:
                    for i in range(n): #还要放更多的皇后，往下一行放吧
                        dfs(row + 1, i)
                        
            board[row] = "." * n #回溯，把本行放下的皇后拿回来
            return
 
        for i in range(n):
            dfs(0, i)
            
        return res


