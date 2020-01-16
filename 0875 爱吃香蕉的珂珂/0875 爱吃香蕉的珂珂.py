#label: 二分查找 difficulty: medium

"""
思路：

二分查找，已知左右极值为ceil（sum（piles）//H），max（piles）,

然后可以用二分法缩小范围。跟1014非常相似。

"""

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        #找右边界
        import math
 
        if len(piles) == 1:
            return int(math.ceil(piles[0] / H))
 
        lo, hi = math.ceil(sum(piles)/H), max(piles)
 
        while(lo < hi):
            mid = (lo + hi)// 2
            
            cnt = 0
            for pile in piles:
                cnt += math.ceil(pile / mid)
                    
            # print k, cnt
            if cnt > H:# 吃得慢了
                lo = mid + 1
            elif cnt <= H:
                hi = mid
                
        return int(lo)


