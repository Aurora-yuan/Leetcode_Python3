#label: array difficulty: easy

"""
思路：

先遍历arr1，

找到arr1里没有在arr2中出现过的元素，把他们丢进left这个数组，

而对于在arr2里出现的元素，用dic这个哈希表记录出现的次数，key是元素的值，val是出现的次数。

然后根据dic里记录的频率，生成结果数组res，

最后把left排序，再拼接到结果数组的后面即可。

"""

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import defaultdict
        res = []
        left = [] #存放没有在arr2里出现过的数字
        set2 = set(arr2) #把arr2转成set，让查找的时间复杂度降低到O(1)
       
        dic = defaultdict(int) #记录arr1中数字出现的频率
        for num in arr1:
            if num in set2:
                dic[num] += 1
            else:
                left.append(num)
 
        for num in arr2:
            res += [num] * dic[num]
 
        left.sort() #按照题目要求把没出现过的元素排序
        return res + left

