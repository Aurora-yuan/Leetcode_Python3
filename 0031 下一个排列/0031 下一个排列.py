#label: array difficulty: medium

"""
思路：

题目要求比当前排列的下一个排列，也就是求 比组合数大的最小的那个组合数，比如 1 4 2 3， 就要找比它大的但是又是最小的 1 4 3 2 。

关键是找数组里的两个下标， i 和 j。

i 代表从nums从尾部往前非递减序列的头， j 代表递增序列里比nums[i - 1]大的最小的元素，

把a[0]到a[i - 1]称作前半部分数，把a[i]到a[n]称作后半部分数，

然后交换a[i - 1]和a[j]，就保障了 新的前半部分数是比之前的前半部分数大的数里面的最小的，因为只把前 i - 1位的最低位a[i - 1]换成了比它大的最小的a[j]，

最后整体翻转后半部分数，因为做了上一步的交换之后， 从a[ i ]往后的序列还是递减的，此时做个翻转，得到的后半部分数就是最小的。



举例：

1 3 5 4 2， 求下一个排列，

观察可得，a[i] = 5, a[i - 1] = 3， a[j] = 4，

前半部分数目前是13， 后半部分数目前是542，

先做交换，可得 1 4 5 3 2， 前半部分数变成14， 后半部分数变成532，

14刚好是比13大的数里最小的那个，

因为现在的532是由5， 3， 2三个数字组成的最大的数，而我们要求的是下一个尽可能小的排列数，所以直接翻转532， 可得235，

组合一下就是14235。

"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #i 代表从nums结尾往前递增序列的头， j代表递增序列里比nums[i - 1]大的最小的元素
        
        l = len(nums)
        for i in range(l - 1, -1, -1):
            if nums[i - 1] < nums[i]:# 找到了需要的 i
                break
        
        if i == 0: # 代表当前不存在下一个更大的序列，整体翻转即可
            nums[:] = nums[::-1]
            return nums
        
        for j in range(l - 1, i - 1, -1):
            if nums[j] > nums[i - 1]: #找到了需要的 j
                break
 
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = nums[i:][::-1]
        return nums
 

