#label: rejection samples difficulty: medium


"""
思路：

leetcode解题报告

"""

from typing import List
import numpy.random as npr

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        x = (npr.random()-0.5)*2
        y = (npr.random()-0.5)*2
        new_r = pow(x,2) + pow(y,2)
        if new_r > 1:
            return self.randPoint()
        x = x * self.radius + self.x_center
        y = y * self.radius + self.y_center
        return [x,y]



# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

