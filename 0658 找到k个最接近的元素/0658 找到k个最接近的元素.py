#label: 二分查找 difficulty: medium

"""
思路：

二分查找找到离x最近的数，然后在附近搜索差最小的数

"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        self.res = []
        def find(arr, left, right, k, x):
            while k>0:
                k-=1
                if left<0:
                    self.res += arr[right:right+k+1]
                    break
                elif right>=len(arr):
                    self.res = arr[left-k:left+1] + self.res 
                    break
                elif abs(arr[left]-x) <= abs(arr[right]-x):
                    self.res = [arr[left]] + self.res
                    left -= 1
                else:
                    self.res += [arr[right]]
                    right += 1
                          
        left, right = 0, len(arr)
        while left<right:
            mid = (left+right)//2
            if arr[mid] == x:
                self.res.append(x)
                find(arr, mid-1, mid+1, k-1, x)
                return self.res
            
            elif arr[mid]>x:
                right = mid
            else:
                left = mid+1
        find(arr, left-1, right, k, x)
        return self.res

    
"""
思路：

排除法（双指针）。

以 arr = [1, 2, 3, 4, 5, 6, 7] , x = 5, k = 3 为例。

思路分析：

1、一个一个删，因为是有序数组，且返回的是连续升序子数组，所以每一次删除的元素一定是位于边界；

2、一共 7 个元素，要保留 3 个元素，因此要删除 4 个元素；

3、因为要删除的元素都位于边界，于是可以使用双指针对撞的方式确定保留区间，即“最优区间”。

"""

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 排除法（双指针）
        size = len(arr)
        left = 0
        right = size - 1

        # 我们要排除掉 size - k 这么多元素
        remove_nums = size - k
        while remove_nums:
            # 调试语句
            # print(left, right, k)
            # 注意：这里等于号的含义，题目中说，差值相等的时候取小的
            # 因此相等的时候，尽量缩小右边界
            if x - arr[left] <= arr[right] - x:
                right -= 1
            else:
                left += 1
            remove_nums -= 1
        return arr[left:left + k]
