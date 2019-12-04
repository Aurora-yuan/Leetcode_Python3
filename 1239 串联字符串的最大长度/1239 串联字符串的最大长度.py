#label: 回溯算法 difficulty: medium

"""
思路：

数据规模暗示回溯，题目问组合明示回溯。

先把arr里所有含有重复字母的元素删掉，然后dfs+回溯找所有可能的组合。

"""

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.res = 0
        visited = set()
        t = []
        for s in arr:
            if len(set(s)) == len(s):
                t.append(s)
        arr = t[:]
 
        def dfs(start, tmp):
            self.res = max(self.res, len(tmp))
            if start >= len(arr):
                return
            for i in range(start + 1, len(arr)):
                if not (set(tmp) & set(arr[i])):
                    visited.add(arr[i])
                    dfs(i, tmp + arr[i])
                    visited.remove(arr[i])
        
        for i, s in enumerate(arr):
            visited.add(s)
            dfs(i, s)
            visited.remove(s)
        
        return self.res


