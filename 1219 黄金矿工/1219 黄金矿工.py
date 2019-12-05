#label: dfs+回溯算法 difficulty: medium

"""
算法
(裸dfs + 回溯)
看题意，操作就是很无脑，然后看到数据范围 15。果断 dfs！
解释：
对应每一个可以出发的点(x, y)，都对其上左下右方向进行搜索，直到走不动为止。 从中记录最大值即为答案。

PS：这种搜索，最好是先判断然后再搜，先搜再判断边界条件的话，多了一层递归，如果是指数级增长的话，多一层容易超时

"""

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j, cur_sum):
            # 递归边界
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] == 0 or (i, j) in visited:  
                return 
            
            visited.add((i, j))
            f[i][j] = max(f[i][j], cur_sum)
            
            # 向四个方向探索，如果有可能的话
            if i > 0:
                dfs(i - 1, j, cur_sum + grid[i-1][j])
            if j > 0: 
                dfs(i, j - 1, cur_sum + grid[i][j-1])
            if i < len(grid) - 1:
                dfs(i + 1, j, cur_sum + grid[i+1][j])
            if j < len(grid[0]) - 1:
                dfs(i, j + 1, cur_sum + grid[i][j+1])

            visited.discard((i, j))
            

        f = [[0] * len(grid[0]) for i in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    visited = set()
                    dfs(i, j, grid[i][j])
        res = 0
        for row in f:
            for col in row:
                res = max(res, col)
        return res                

