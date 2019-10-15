#label: 双指针 difficulty: easy

"""
这题用python就体现出了python的优势了。

（1）从collections集合模块中引入集合类Counter 
（2）Counter(a)可以打印出数组a中每个元素出现的次数 
（3）Counter(a).most_common(2)可以打印出数组中出现次数最多的元素。参数2表示的含义是：输出几个出现次数最多的元素。

"""

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
    
        c = collections.Counter(nums)
        count = 0
        if k < 0:
            return 0
        if k == 0:
            for item in c.keys():
                if c[item] > 1:
                    count +=1
            return count
        else:
            for item in c.keys():
                if item + k in c:
                    count += 1
            return count

