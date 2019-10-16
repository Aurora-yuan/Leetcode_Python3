#label: 双指针 difficulty: easy

"""
思路：

利用额外空间直接合并即可。

声明双指针p1, p2，分别指向nums1和nums2的起点，

比较nums1[p1]和nums2[p2]的大小，把小的插入到temp里，并且指针后移一位，

当p1 或者 p2指向结尾的时候，把剩下的元素都插入到temp里，

最后根据题目要求把temp里的元素复制到nums1。
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        p1 = 0
        p2 = 0
        while(p1 < m and p2 < n):
            if (nums1[p1] <= nums2[p2]):
                temp.append(nums1[p1])
                p1 += 1
            else:
                temp.append(nums2[p2])
                p2 += 1
        
        while(p1 < m):
            temp.append(nums1[p1])
            p1 += 1
        while(p2 < n):
            temp.append(nums2[p2])
            p2 += 1
        
        for i in range(0, m + n ):
            nums1[i] = temp[i]


