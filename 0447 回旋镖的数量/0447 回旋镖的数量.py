#label: hashmap difficulty: easy

"""
我们注意到我们这里有一个中间变量i，每次都是和i比较距离。那么我们可以将和i所有距离的点加到一个record中，

然后通过查找和这个i的距离相同的点的个数（必须>=2），计算出这些点对应有多少种组合即可。

"""

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def dist(point1,point2):
            return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
        
        result = 0
        for i in points:
            record = {}
            for j in points:
                if j != i:
                    distance = dist(i,j)
                    record[distance] = record.get(distance,0) + 1
                    
            for val in record.values():
                if val >= 2:
                    result += (val - 1) * val
                    
        return result
