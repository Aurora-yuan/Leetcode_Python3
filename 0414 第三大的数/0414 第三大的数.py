#label: array difficulty: easy

"""
解题思路：

1.时间复杂度必须是O(n)，那么sort()方法不能使用（sort()时间复杂度为O(nlogn)）。

2.去掉重复元素，可以使用集合(set)，将列表转化为集合

3.删除最大和次大的元素，可以使用remove()

"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #将列表转化为集合
        nums = set(nums)
        if len(nums) == 1:
            return list(nums)[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            #删除最大和次大的元素
            for i in range(2):
                nums.remove(max(nums))

            return max(nums)
