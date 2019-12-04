#label: random difficulty: medium

import random
import bisect
 
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.sw = []
        w_sum = 0
 
        for ww in self.w:
            w_sum += ww
            self.sw.append(w_sum)

    def pickIndex(self) -> int:
        #同leetcode497,bisect.bisect_left和random.choice(weight)都行
        return bisect.bisect_left(
            self.sw, random.randint(1, self.sw[-1]))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
