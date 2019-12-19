#label: 回溯算法 difficulty: medium

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]: 
        # 思路一： 调库
        # import itertools
        # return list(itertools.combinations(range(1,n+1),k))
        
        #思路二： 回溯
        res = []
        def dfs(t, cnt, tmp):
            if cnt == 0:
                res.append(tmp[:])
 
            for i in range(t + 1, n + 1):
                dfs(i, cnt - 1, tmp + [i])
            
        dfs(0, k, [])
        return res




