#label: hashmap difficulty: medium

"""
思路：

数独有效必须满足三个条件：

1. 每一行1-9

2. 每一列1-9

3. 每个3*3的方块1-9

所以可以用三个字典来记录行、列和方块的已有元素情况。比如

row[1] = [1, 3, 5]就代表第一行已经出现了1， 3和5，如果下一个3又出现在了第一行，就说明数独无效。

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        row, column, squre  = defaultdict(set), defaultdict(set), defaultdict(set)
 
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit(): #排除掉空的情况
                    if board[i][j] in row[i] or board[i][j] in column[j] or (board[i][j]) in squre[(i // 3, j // 3)]:
                        return False
                    else:
                        row[i].add(board[i][j])
                        column[j].add(board[i][j])
                        squre[(i // 3, j // 3)].add(board[i][j])
        return True


