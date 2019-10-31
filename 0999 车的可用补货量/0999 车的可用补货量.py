#label: array difficulty: easy

"""
思路：

定义一个方向数组，类似{{0，1}，{0，-1}，{1，0}，{-1，0}}这样的。但是也是有瑕疵的，就是对每一个方向上的查找都要检查行和列有没有溢出，

但是我们知道，其实不用都检查，比如你向上（北）检查，列是固定的，一定不会溢出，没必要检查。

"""

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    #从该点的四个方向上进行查找
                    for n,m in [[0,1],[1,0],[0,-1],[-1,0]]:
                        x = i + n
                        y = j + m
                        while 0<x<len(board) and 0<y<len(board[0]):
                            if board[x][y] == "B":
                                break
                            elif board[x][y] == 'p':
                                res += 1
                                break
                            x = x + n
                            y = y + m
        return res
