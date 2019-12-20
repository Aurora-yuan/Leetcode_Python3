#label: dfs + 回溯算法 + 剪枝 difficulty: medium

class Solution(object):
    def combinationSum2(self, c, t):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = list()
        l = len(c)
        def dfs(start, tmp):
            s = sum(tmp)
            if s == t:#满足题目要求
                tt = sorted(tmp)
                if tt not in res:#避免重复
                    res.append(tt[:])
                return
            if start >= l:
                return
 
            for i in range(start, l):
                
                if c[i] > t or s + c[i] > t:#剪枝
                    continue
                
                tmp.append(c[i])
                dfs(i + 1, tmp) #下一层
                tmp.pop()#回溯
                    
        for i,x in enumerate(c):
            dfs(i, list())
            
        return res

