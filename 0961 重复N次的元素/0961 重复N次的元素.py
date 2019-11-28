#label: count difficulty: easy

"""
第一种思路：

已知这个重复元素出现N次，而总共只有2N的元素，所以排序后该重复元素必定出现在中点附近，比如[1,3,3,5], [1,1,2,4], [1,2,5,5]，

然后因为中间有两个数，所以判断一下到底是哪一个就OK

第二种思路：

直接查找每个元素出现的次数，出现N次的那个元素就直接返回

"""

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for a in A:
            if A.count(a) == int(len(A)/2 ):
                return a
                

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        half_l = len(A) / 2
        temp = sorted(A)
        return temp[half_l] if temp[half_l] == temp[half_l + 1] else temp[half_l - 1]
