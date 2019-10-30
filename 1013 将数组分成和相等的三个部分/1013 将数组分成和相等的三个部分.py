#label: maths difficulty: easy

"""
思路：

从头到尾 线性扫描，如果能找到当前这一段的和cur==target，那就给count + 1， 然后归零cur

如果扫完了发现刚好有三个count，就代表True。

"""

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        target = sum(A) // 3
        cur = 0
        count = 0
        for i in A:
            cur += i
            if cur == target:
                cur = 0
                count += 1
        return count == 3
