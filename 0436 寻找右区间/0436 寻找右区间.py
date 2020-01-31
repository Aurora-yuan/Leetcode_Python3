#label: 二分查找 difficulty: medium

"""
思路：

要找最小的起始点，所以需要按每个区间的起始点排序，

又因为结果数组里需要存储原数组里每个区间的下标，所以需要一个哈希表，key是每个区间， val是每个区间的原始下标。

排好序之后，在有序的数组里二分查找即可。

时间复杂度：O（NlogN）

空间复杂度：O（N）

"""

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic = {}
        for i, (start, end) in enumerate(intervals):
            dic[start] = i
 
        res = [-1 for _ in range(len(intervals))]
 
        l = [interval[0] for interval in intervals]
        l = sorted(l, key = lambda x:x)
 
        for i, (start, end) in enumerate(intervals):
            idx = bisect.bisect_left(l, end) #找l数组里第一个 >= end 数的下标
            if idx < len(l): # 如果找到了下标，即有解
                res[i] = dic[l[idx]]
                
        return res


