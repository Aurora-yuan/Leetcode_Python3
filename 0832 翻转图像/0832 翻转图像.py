#label: array difficulty: easy

#思路一：两趟扫描法

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i , x in enumerate(A):
            A[i] = x[::-1]
            
        for row in A:
            for i, x in enumerate(row):
                row[i] = 1 - x
                
        return A


#思路二：一趟扫描法

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i , x in enumerate(A):
            A[i].reverse()
            A[i] = [(1 - j) for j in A[i]]
                
        return A

