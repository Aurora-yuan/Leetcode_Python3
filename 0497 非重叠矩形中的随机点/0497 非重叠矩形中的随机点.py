#label: random difficulty: medium

import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        for [x_bl,y_bl,x_tr,y_tr] in self.rects:
            self.weights.append((x_tr - x_bl + 1)*(y_tr - y_bl + 1))

    def pick(self) -> List[int]:
        [x_bl, y_bl, x_tr, y_tr] = random.choices(
            self.rects, weights=self.weights)[0]  #使用random.choices() 根据权重选择矩形
        #在所选的矩形中随机生成点
        res = [
            random.randrange(x_bl, x_tr + 1),
            random.randrange(y_bl, y_tr + 1)
        ]
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()


