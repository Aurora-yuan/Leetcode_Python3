#label: 分治算法 difficulty: medium

"""
思路：

根据题意，

每一行的第一个数字是这一行最小的数，

每一列的最后一个数字是这一列最大的数，

所以不妨从矩阵的左下角出发，

如果target比当前元素小，则说明target肯定不在这一行，因为 每一行的第一个数字是这一行最小的数，

因此最后一行可以被去掉。

如果target比当前元素大，则说明target肯定不在这一列，因为 每一列的最后一个数字是这一列最大的数，

因此第一列可以被去掉。

按照以上步骤依次处理，如果最后矩阵都为空了，还没有找到target，

就说明target不存在于matrix中。

"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        
        i, j = m - 1, 0
        while 0 <= i < m and 0 <= j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False


