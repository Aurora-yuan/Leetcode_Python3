#label: random difficulty: medium

"""
思路：

这道题的思路为将2维矩阵降为一维，从而方便使用random函数获取位置。由于我们只对值为0的元素进行翻转，所以需要避免已经被翻转过的元素。

在代码中我们使用了一个set（因为我们只关心存在与否）来对翻转过的位置进行存储。

"""

import random

class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.cols = n_cols
        self.end = n_rows * n_cols - 1
        self.fliped = set()
        self.start = 0

    def flip(self) -> List[int]:
        while True:
            position = random.randint(self.start, self.end)
            if position not in self.fliped:
                self.fliped.add(position)
                return divmod(position, self.cols)



    def reset(self) -> None:
        self.fliped = set()


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()

