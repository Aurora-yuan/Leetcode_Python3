#label: dfs difficulty: medium

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(start, cnt, target, tmp):
            if target < 0:
                return
            if target == 0:
                if cnt == 0:
                    res.append(tmp)
                else:
                    return
                
            for num in range(start, 10):
                #visited.add(num)
                dfs(num + 1, cnt - 1, target - num, tmp + [num])
                #visited.remove(num)
        #visited = set()        
        dfs(1, k, n, [])
        return res


