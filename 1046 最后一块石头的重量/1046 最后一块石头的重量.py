#label: 贪心算法 difficulty: easy

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while( len(stones) > 1):
            stones.sort()
            x, y = stones[-2], stones[-1]
            if x == y:
                stones = stones[:-2]
            else:
                stones = stones[:-2] + [y - x]
        return 0 if len(stones) == 0 else stones[0]


