#label: maths difficulty: easy

"""
思路：

按直白的题意出发，先判断有没有相同的点，再判断三点共不共线。

共线的判断方法是，计算点1和点0的斜率，再计算点2和点1的斜率，看两个斜率相不相同。

坑点有三个：

1. 除法计算时除数不能为0；   

2. 斜率可能是浮点数所以要用1.0 *一下把计算结果转成浮点数； (python3中不用)

3. 两个浮点数比相同不能用等号，要用相减的差和0.0001的比大小来表示

"""

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        #考虑三点各不相同
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False
        
        x0, x1, x2 = points[0][0], points[1][0], points[2][0]
        y0, y1, y2 = points[0][1], points[1][1], points[2][1]
        
        #考虑除数不能为0
        if x0 == x1 or x2 == x1:
            return x0 != x2
        
        #考虑不存在三点共线的情况
        return abs ((y2 - y1) / (x2 - x1) - (y1 - y0) /(x1 - x0)) > 0.0001


