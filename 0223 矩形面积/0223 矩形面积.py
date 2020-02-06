#label: string difficulty: medium

"""
思路：

思路比较简单，

先判断一下存不存在重叠的部分，

判断的依据是： 如果【A, C】和【E, G】存在交集 并且 【B, D】和【F， H】存在交集，则说明存在重叠面积，

再分别计算出两个矩形各自的面积， 加在一起最后减去重叠部分的面积就是总面积了。

"""

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        # [A, C]和[E, G]取交集, [B, D]和[F, H]取交集
        if min(C, G) - max(A, E) < 0 or min(D, H) - max(B, F) < 0:
            S_overlap = 0
        else:
            S_overlap = (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        S_first_square = (D - B) * (C - A)
        S_second_square = (H - F) * (G - E)
        # print S_second_square, S_first_square, S_overlap
        return S_second_square + S_first_square - S_overlap


