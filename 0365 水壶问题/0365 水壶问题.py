#label: dfs/math difficulty: medium

"""
思路：

官方题解包含两种方法：dfs + 数学解题

"""

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # 方法一：DFS
        stack = [(0,0)]
        self.seen = set()
        while stack:
            remain_x,remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if  (remain_x,remain_y) in self.seen:
                continue
            self.seen.add((remain_x,remain_y))
            # 把 X 壶灌满。
            stack.append((x, remain_y))
            # 把 Y 壶灌满。
            stack.append((remain_x, y))
            # 把 X 壶倒空。
            stack.append((0, remain_y))
            # 把 Y 壶倒空。
            stack.append((remain_x, 0))
            # 把 X 壶的水灌进 Y 壶，直至灌满或倒空。
            stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
            # 把 Y 壶的水灌进 X 壶，直至灌满或倒空。
            stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
        return False

        #方法二：数学方法
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x+y == z
        return z % math.gcd(x,y) == 0
