#label: maths difficulty: easy 

"""
每次移动n-1个元素，使其+1，相当于把最大的元素–1，我们的目标是把所有的元素搞相等，也就是每次把最大的元素-1 直到所有元素都等于最小元素即可。

故总的运算次数等于所有元素与最小元素的差的和

"""

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=len(nums)
        min_val=min(nums)
        res=0
        for i in range(n):
            res+=nums[i]-min_val
        return res


    class Solution:
        def minMoves(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            return sum(nums) - len(nums) * min(nums)

