#label: dynamic programming difficulty: medium

"""
思路：

看到求什么什么的连续子序列，一般都是DP，而且DP【i】代表的还是以nums[i]结尾的连续子序列的某种状态。

这题也不例外……

基础的dpmax用来表示乘积最大的子序列的乘积，

比较特殊的地方在于，因为是算乘积而且没有限定输入的范围，所以需要考虑负数的情况。

所以要额外开一个dpmin表示乘积最小的子序列的乘积。

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        dpmax = [0 for _ in range(l)]
        dpmin = [0 for _ in range(l)]
        
        dpmax[0] = nums[0]
        dpmin[0] = nums[0]
        
        for i in range(1,l):
            dpmax[i] = max(nums[i],dpmax[i-1]*nums[i],dpmin[i-1]*nums[i])
            dpmin[i] = min(nums[i],dpmax[i-1]*nums[i],dpmin[i-1]*nums[i])
            
        return max(dpmax)
