# label: 暴力+回溯算法 difficulty: difficult

class Solution:
    def isValue(self,board,x,y):
        #检查填入的坐标是否与行中已有元素相等
        from collections import defaultdict
        row, column, square = defaultdict(list),defaultdict(list),defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in row[i] or board[i][j] in column[j] or board[i][j] in square[(i//3,j//3)]:
                        return False

                    else:
                        row[i].append(board[i][j])
                        column[j].append(board[i][j])
                        square[(i//3,j//3)].append(board[i][j])
        return True
        
    def dfs(self,board):
        #遍历每一个坐标
        for i in range(9):
            for j in range(9):
                #找board里的需要填入的位置
                if board[i][j] == '.':
                    #从可选之间选一个
                    for k in '123456789':
                        board[i][j] = k
                        #在if的时候调用递归
                        #如果这个递归可以返回true并且当前填入的数字也没毛病
                        #则证明我们解完了数独
                        if self.isValue(board,i,j) and self.dfs(board):
                            return True
                        #到这个位置说明填入的数不太行，所以把它先空着。
                        board[i][j] = '.'
                    #进行完当前可选的所有数字都不行，说明上一次决策有问题，返回false
                
                    return False
        #所有'.'都填满，并且没毛病，返回true
        return True
        
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(board)
