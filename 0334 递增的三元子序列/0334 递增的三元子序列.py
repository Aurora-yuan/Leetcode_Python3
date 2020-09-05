#label: array difficulty: medium

"""
思路一：

只限于本题的思路。

用两个变量 r1, r2 分别记录第一小和第二小的数。然后遍历 nums。只要碰到比 r1 小的数我们就替换掉 r1，碰到比 r1 大但比 r2 小的数就替换 r2。

只要碰到比 r2 大的数就已经满足题意了。

"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        r1, r2 = sys.maxsize, sys.maxsize
        for n in nums :
            if n <= r1 : r1 = n
            elif n <= r2 : r2 = n
            else : return True
        return False

