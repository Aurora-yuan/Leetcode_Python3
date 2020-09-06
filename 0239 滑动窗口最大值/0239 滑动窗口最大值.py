#label: sliding window difficulty: diffcult

"""
思路一：

暴力求解。

每次把window数组找出来然后暴力求最大值。

"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
 
        if not nums:
            return []
 
        temp,res = list(), list()
        for index in range(len(nums) - k + 1):
            temp = nums[index: index + k]
            max_val = max(temp)
            
            res.append(max_val)
        
        return res

"""
思路二：

Sliding Window法。

维护window这个数组，使得在任意时刻，window【0】都是当前Window内最大值的下标。

并且window从左到右恰恰是第一大、第二大、。。。。。第K大的元素

维护过程为：

(Window代表窗口， window代表窗口的数组）

1. 如果window不为空，并且 window[0] 比 i - k 小 （这就说明window[0]在当前Window的左界的左侧，应该被踢出去）， 把window【0】弄出去

2. 把从队尾倒着数的每个比item 大的元素都弄出去

3. 把item 弄进Window

4. 如果index >= k - 1， 就说明Window size 已经有k了，可以输出答案了。因为如果 index < k - 1， 说明Window size还没到k。

"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
 
        window = []
        res = []
        for i in range(len(nums)):
            if window and window[0] <= i - k: #当前window头应该被弹出
                window.pop(0)
                
            while window and nums[window[-1]] < nums[i]: #比 nums[i] 小的都不要，因为只要窗口的最大值
                window.pop()
                
            window.append(i) #当前数的下标 入队列
            if i >= k - 1: #已经可以得到一个长度为k的队列
                res.append(nums[window[0]])
        return res

