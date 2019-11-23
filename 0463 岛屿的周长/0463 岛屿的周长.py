#label: DFS difficulty: easy

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # DFS 四方向，如果碰壁或者是0 边就 + 1
 
        m= len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        
        def check(i, j):
            temp = 0
            if i == 0 or grid[i - 1][j] == 0:
                temp += 1
            if j == n - 1 or grid[i][j + 1] == 0:
                temp += 1
            if i == m - 1 or grid[i + 1][j] == 0:
                temp += 1
            if j == 0 or grid[i][j - 1] == 0:
                temp += 1
            return temp
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += check(i, j)
        return res

