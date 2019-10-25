#label: maths difficulty: easy

class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        #统计奇数和偶数的个数，返回比较少的个数
        l1 = 0
        l2 = 0
        for i in chips:
            if i%2 == 0:
                l1 += 1
            else:
                l2 += 1
        return min(l1,l2)

