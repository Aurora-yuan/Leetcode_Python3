#label: maths difficulty: easy


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]
        # 求斜率 k
        if x1 == x2:
            k = 0
        else:
            k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1
        
        for i in range(2, len(coordinates)):
            x = coordinates[i][0]
            y = coordinates[i][1]
            if k * x + b != y:
                return False
            
        return True

