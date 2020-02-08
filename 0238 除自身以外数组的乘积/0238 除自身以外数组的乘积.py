#label: array difficulty: medium

"""
思路：

不能用除法，那只能用乘法统计其他元素的乘积了，

一共扫两趟，

第一趟从左往右走，开一个数组叫left记录除第一个元素外，其他每个元素的所有左边元素的乘积，left[0] = 1

比如对于[1,2,3,4]，我们有left = [1,1, 2, 6]，

类似的，第二趟从右往左走，开right数组记录所有右边元素的乘积，right[-1] = 1

比如对于[1,2,3,4]，我们有right = [24, 12, 4, 1]

最后把left和right对位相乘，就是需要的结果。

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= tmp
            tmp *= nums[i]
        return res


