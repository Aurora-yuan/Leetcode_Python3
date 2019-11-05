#label: array difficulty: easy

"""
思路一： 

哈希表，最简单直接，但是需要用到额外空间

"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)+1
        h = [0]*l
        for i in nums:
            h[i]=1
        ans = []
        
        for i in range(1,l):
            if h[i]==0:
                ans.append(i)
        return ans


“”“
思路二：

解题思路：

不用到额外空间，则需要在原数组上进行修改。因为有这一条件1 ≤ a[i] ≤ n （n为数组长度），最大的元素值不超过数组长度，

所以可以考虑将每个元素排在相应的位置上，，例如若元素为2，则放在数组的第二个位置上，即索引为1处。比较i+1和nums[i]的值是否相等，若不相等输出i+1

”“”

class Solution(object):
    def findDisNum(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i] - 1]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i += 1

        res = []
        for i in  range(len(nums)):
            if i + 1 != nums[i]:
                res.append(i+1)
        return res
           
