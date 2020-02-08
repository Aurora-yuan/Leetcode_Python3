#label: array difficulty: medium

"""
思路：

拿每个元素的绝对值作为下标，

如果是第一次访问该元素，那么nums[p - 1] > 0， 把nums[p]取反，

如果是第二次访问nums[p - 1]， 此时的nums[p - 1]就是负的。

"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = list()
        for i, x in enumerate(nums):
            p = abs(x)
            # print nums, p
            if nums[p - 1] < 0: #说明p重复了
                res.append(p)
            else:
                nums[p - 1] *= -1
                
        return res


