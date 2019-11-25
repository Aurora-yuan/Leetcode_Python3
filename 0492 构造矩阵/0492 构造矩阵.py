#label: math difficulty: easy

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        for width in range(int(math.sqrt(area)), 0, -1):
            if area % width == 0:
                return [area/width, width]

