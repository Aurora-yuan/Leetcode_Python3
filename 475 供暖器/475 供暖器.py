#label: 二分查找 difficulty: easy
"""
解题思路：
排序（Sort） + 二分查找（Binary Search）

升序排列加热器的坐标heaters

遍历房屋houses，记当前房屋坐标为house：

利用二分查找，分别找到不大于house的最大加热器坐标left，以及不小于house的最小加热器坐标right
    
则当前房屋所需的最小加热器半径radius = min(house - left, right - house)
    
利用radius更新最终答案ans

"""

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        #bisect用法：https://www.jianshu.com/p/b626dbaa1200
        ans = 0
        heaters.sort()
        for house in sorted(houses):
            radius = 0x7FFFFFFF
            le = bisect.bisect_right(heaters,house)
            if le>0:
                radius = min(radius,house-heaters[le-1])
            ge = bisect.bisect_left(heaters,house)
            if ge<len(heaters):
                radius = min(radius,heaters[ge]-house)
            ans = max(ans,radius)
        return ans
