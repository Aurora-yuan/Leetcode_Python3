#label: 二分查找 difficulty: medium

"""
思路：

考虑一下重复元素会造成什么样的影响，
如果nums[0] != nums[-1]：

两次二分查找都可以正常进行，直接调用上一题的答案就可以
如果nums[0] == nums[-1] == target：

直接找到了target，返回True即可
如果nums[0] == nums[-1] != target:

首先在找分割点的过程中，情况会变得更加复杂，比如[1,3,1,1,1]，第一次循环得到的mid是nums[(0 +4) // 2] = nums[2] = 1，那么现在问题来了，这个1因为和nums[0]相等，又和nums[-1]相等，所以无法直接确定它到底落在哪一段，因为还有可能是[1,1,1,3,1]这种情况。
所以为了确认分割点落在哪一段上，就需要遍历mid左右的某一段。(PS： 如果偷懒不想写直接一趟线性扫描找target也是可以过OJ的，而且速度还不慢……）

比如[1,3,1,1,1]这个数组，从mid = 2向尾部进行遍历，直到到达数组尾部或者找到第一个不是nums[0]的元素为止。如果遍历的过程中从mid 到 len（nums） - 1所有元素都是相同的，就说明mid右侧不需要考虑了，因为我们的前提条件是nums[0] == nums[-1] != target。

又比如[1,1,1,3,1]这个数组，从mid = 2向尾部进行遍历，发现下一个元素就是3，说明mid的左侧全部等于nums[0]，也无需考虑。

在极端情况下，可能会遍历整个数组，所以这一步的时间复杂度是O（n）

成功找到了分割点的坐标之后，数组可以被分成两个有序的部分，接着用常规的二分查找就可以找Target。

总体的时间复杂度是O(N) + O(logN) = O(N)

"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #如果第一个数和最后一个数不相等，那么跟上一题没有区别
        #如果第一个数和最后一个数相等，而且等于target，return true
        #如果第一个数和最后一个数相等，但是不等于target，在最坏的情况下就需要遍历两个升序数组的某一个，已确定target有可能落在哪一段，极端情况时间复杂度会降低到0(N)
        if not nums:
            return False
        if nums[0] != nums[-1]:
            return self.search1(nums, target)
        if nums[0] == nums[-1]:
            if nums[0] == target:
                return True
            else:
                # for num in nums: #偷懒就可以这么写……直接上O(N)的算法
                #     if num == target:
                #         return True
                # return False
                return self.search2(nums, target)
        
    def search1(self, nums, target): #上一题的解答，两次二分查找分别找旋转点和结果
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return True if nums[0] == target else False
        
        lo, hi = 0, len(nums) - 1
        while(lo <= hi):
            mid = (lo + hi) // 2
            if mid + 1 < len(nums) and nums[mid] > nums[mid +1]: #旋转点为mid
                break
            if nums[mid] <= nums[-1]:
                hi = mid - 1
            elif nums[mid] >= nums[0]:
                lo = mid + 1
                
        if lo > hi:#没有旋转
            lo, hi = 0, len(nums) - 1
        else:
            if target >= nums[0]:
                lo, hi = 0, mid
            else:
                lo, hi = mid + 1, len(nums) - 1

        while(lo <= hi):
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False
    
    def search2(self, nums, target):#这种情况下nums[0] == nums[-1]
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return True if nums[0] == target else False
        
        lo, hi = 0, len(nums) - 1
        while(lo <= hi):
            mid = (lo + hi) // 2
            if mid + 1 < len(nums) and nums[mid] > nums[mid +1]:
                break
            if nums[mid] == nums[0]: #无法确定mid落在哪一段
                i = mid
                while(i < len(nums) - 1 and nums[i] == nums[i + 1]):
                    i += 1
                if i == len(nums) - 1:#整个右段都找完了，全部跟nums[0]一样，所以target肯定落在左侧，也就是0 ~ mid这一段
                    hi = mid - 1
                else:
                    lo = mid + 1
                
            if nums[mid] < nums[-1]:
                hi = mid - 1
            elif nums[mid] > nums[0]:
                lo = mid + 1    
        # print nums[mid]
        if target > nums[mid]:
            return False #因为mid一定是最大的那个数
        elif target == nums[mid]: #找到了就直接返回
            return True
        elif target < nums[mid]: #还需要二分查找，现在要确认找左侧还是找右侧
            if target > nums[0]: #在左侧找
                lo, hi = 0, mid - 1
            else: #在右侧找
                lo, hi = mid + 1, len(nums) - 1
            
        while(lo <= hi):
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False


