#label: maths difficulty: easy

"""
解题思路：
先把数组排序，如果数组里全是正数或者三个最大的数字里有一个负数，那么三个最大的数相乘就是答案了。
但是如果数组里有两个以上负数，那么就要比较最大三个数的乘积和两个最小数乘以最大数的乘积，谁大谁就是答案。
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if nums[-1]*nums[-2]*nums[-3] > nums[0]*nums[1]*nums[-1]:
            return nums[-1]*nums[-2]*nums[-3]
        else:
            return nums[0]*nums[1]*nums[-1]

