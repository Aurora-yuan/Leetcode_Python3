#label: maths difficulty: easy

"""
思路

已知三个点坐标可以通过坐标公式求三角形面积：

面积公式为
s=(x1∗y2+x2∗y3+x3∗y1−x1∗y3−x2∗y1−x3∗y2)/2

通过暴力解法，循环3次

"""

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxarea = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for z in range(j+1, len(points)):
                    tmp = (points[i][0] * points[j][1] + points[j][0] * points[z][1] + 
                           points[z][0] * points[i][1] - points[i][0] * points[z][1] - 
                           points[j][0] * points[i][1] - points[z][0] * points[j][1]) / 2
                    
                    maxarea = max(maxarea, abs(tmp))
                          
        return maxarea
