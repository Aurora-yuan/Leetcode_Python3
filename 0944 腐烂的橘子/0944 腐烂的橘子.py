#label: BFS difficulty: easy

"""
思路：

这种需要一圈一圈往外传播的一般用BFS解，

先找到起始所有腐烂的橘子，

然后循环处理，把新腐烂的橘子加入下一次循环的队列中，

当下一次循环的队列为空时，说明不能继续腐烂了，

判断一下还有没有新鲜的橘子，如果有，就返回-1，否则返回分钟数

"""

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        rotlist = list()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotlist.append([i, j])
        minute = 0
        while(rotlist):
            newrotlist = list()
            for rotnode in rotlist:
                x0 = rotnode[0]
                y0 = rotnode[1]
                
                for k in range(4):
                    x = x0 + dx[k]
                    y = y0 + dy[k]
                    
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        newrotlist.append([x,y])
            if not newrotlist:
                break
                
            rotlist = newrotlist[:]
            minute += 1
            
        for row in grid:
            for i in row:
                if i == 1:#还有新鲜的
                    return -1
        return minute

