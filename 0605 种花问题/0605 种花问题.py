#label: array difficulty: easy

"""
解题思路：

在列表两端分别添加0用来处理边界问题，然后遍历列表，如果当前值是0，且前面和后面一个均为0，则将当前值改为1，并在可以种花的个数上加1.

"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                count += 1
                flowerbed[i] =1
        return count>=n
            
