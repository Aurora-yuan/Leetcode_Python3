#label: array difficulty: easy

"""
思路：

线性扫描，遇到一个0就把它后面的数依次往后挪一位，然后加一个0到这个0后面。

"""

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        i = 0
        while i < l:
            if arr[i] == 0:
                for j in range(l-1,i+1,-1):
                    arr[j] = arr[j-1]
                if i+1 < l:
                    arr[i+1] = 0
                i += 2
            else:
                i += 1
        
