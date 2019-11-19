#label: BFS difficulty: easy

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        #BFS
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        res = [[r0,c0]]
        queue = res[:]
        visited = [[0 for i in range(101)] for j in range(101)]
        visited[r0][c0] = 1
        
        while queue:
            next_queue = list()
            
            for node in queue:
                x0,y0 = node[0],node[1]
                for k in range(4):
                    x = x0 + dx[k]
                    y = y0 + dy[k]
                    if x<0 or x>=R or y<0 or y>=C:
                        continue
                    if visited[x][y] == 1:
                        continue
                    next_queue.append([x,y])
                    res.append([x,y])
                    visited[x][y] = 1
            queue = next_queue[:]
            
        return res
                    
