#label: array difficulty: easy

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #逆转前n - k个数，再逆转后k个数，最后总体逆转
        n = len(nums)
        k = k % n
        
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        reverse(0, n - k - 1)
        reverse(n - k, n - 1)
        reverse(0, n - 1)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #每次把第一个数放到最后去，一共放n - k次
        for i in range(len(nums) - k % len(nums)):
            tmp = nums[0]
            nums.pop(0)
            nums.append(tmp)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #每次把最后一个数放到最前面，放k次
        for i in range(k):
            # tmp = nums[0]
            tmp = nums.pop()
            nums.insert(0, tmp)

