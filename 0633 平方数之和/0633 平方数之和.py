#label: maths difficulty: easy

"""
思路：

设k = int(sqrt（c）), 如果c自身就是一个完全平方数，即k * k = c，则 c 可以和 0 组，所以返回True。

如果c不是一个完全平方数，

那么可以把1 ~ k的平方记录在一个数组record里，record = [1, 4, 9, ......., k * k]

然后线性扫描record， 对record里的每一个元素x，判断一下 c - x 在不在record里，如果在，就返回True。

如果找不到就返回False。

时空复杂度分析：

record数组长度为K = sqrt（N），每个元素都要扫到；判断补集在不在用二分查找 logK；

所以时间复杂度一共是O(KlogK)， K = sqrt(N)

空间复杂度 O(K)

"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == (int(c ** 0.5) ** 2):
            return True
        
        record = list()
        for i in range(1, int(c ** 0.5) + 1):
            record.append(i **2)
        
        def find(n):
            lo, hi = 0, len(record) - 1
            
            while(lo <= hi):
                mid = (lo + hi) // 2
                if record[mid] == n:
                    return True
                elif record[mid] > n:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return False
 
        for i, x in enumerate(record):
            if find(c - x):
                return True
        return False

