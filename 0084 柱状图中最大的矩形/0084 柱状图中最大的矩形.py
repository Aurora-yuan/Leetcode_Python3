#label: stack difficulty: difficult

"""
思路：

利用递增栈找到矩形的左右边界。

详细解释可以看这篇文章，写的很好：https://blog.csdn.net/Zolewit/article/details/88863970

"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = list()
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                res = max(res,(i-stack[-1]-1)*heights[top])

            stack.append(i)

        return res
