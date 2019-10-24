#label: maths difficulty: easy

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    n += 2 + 4 * grid[i][j]
                if i > 0:
                    n -= 2 * min(grid[i][j], grid[i - 1][j])
                if j > 0:
                    n -= 2 * min(grid[i][j], grid[i][j - 1])
        return n


