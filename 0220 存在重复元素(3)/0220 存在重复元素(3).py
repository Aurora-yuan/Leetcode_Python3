#label: Ordered Map difficulty: medium

"""
第一种思路：

暴力解，结果只能过40/41的case，最后超时。

"""

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        dic = dict()
        for i, num in enumerate(nums):
            for j in range(max(0, i - k), min(len(nums), i + k)):
                if j == i:
                    continue
                if abs(nums[j] - nums[i]) <= t:
                    # print nums[j], nums[i]
                    return True
        return False


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        record = []
        for i, num in enumerate(nums):
            record.append([num, i])
        record.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if record[j][0] - record[i][0] > t:
                    break
                if abs(record[i][1] - record[j][1]) <= k:
                    return True
        return False

