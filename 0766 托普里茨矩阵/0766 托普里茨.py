#label: array difficulty: easy

"""
思路一：

遍历数组，判断每一个元素和它右下方元素（行数和列数均加一）是否相等，注意每一行最后一个元素以及最后一行元素无需比较（已经比较过了），

所以遍历时，行数和列数都要减1.

"""

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True

别人的做法,不用每个元素比较一次，可以进行整行比较，这样只用一重循环。

        for i in range(1,len(matrix)):
            if matrix[i][1:]!=matrix[i-1][0:-1]:
                return False
        return True
