#label: array difficulty: medium

"""
思路：

先转置再左右对称翻转。

比如：

输入为：[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

转置可以得到:[

[1,4,7],

[2,5,8],

[3,6,9],

]

再对每一行进行翻转，即可得到答案:[

[7,4,1],

[8,5,2],

[9,6,3],

]

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #先转置再左右对称翻转
        if not matrix or not matrix[0]:
            return matrix
        n = len(matrix)
        
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                
        for row in matrix:
            for i in range(n//2):
                row[i],row[n-1-i] = row[n-1-i],row[i]
                
        return matrix
