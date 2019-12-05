#label: 回溯算法 difficulty: medium

import itertools
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res=0
        n=len(tiles)
        for i in range(1,n+1):
            res+=len(set(itertools.permutations(tiles,i)))
        return res

