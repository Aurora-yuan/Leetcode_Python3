#label: 并查集 difficulty: medium


class UnionFindSet(object):
    def __init__(self,grid):
        m,n = len(grid),len(grid[0])
        self.roots = [i for i in range(m)]
        self.rank = [0 for i in range(m)]
        self.count = n
     
    def find(self,member):
        tmp = []
        while member != self.roots[member]:
            tmp.append(member)
            member = self.roots[member]
            
        for root in tmp:
            self.roots[root] = member
        return member
    
    def union(self,p,q):
        parentP = self.find(p)
        parentQ = self.find(q)
        if parentP != parentQ:
            if self.rank[parentP] > self.rank[parentQ]:
                self.roots[parentQ] = parentP
            elif self.rank[parentP] < self.rank[parentQ]:
                self.roots[parentP] = parentQ
            else:
                self.roots[parentQ] = parentP
                self.rank[parentP] -= 1
            self.count -= 1

            
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M and not M[0]:
            return 0
        
        ufs = UnionFindSet(M)
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    ufs.union(i,j)
                    
        return ufs.count
