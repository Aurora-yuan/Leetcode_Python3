#label: array difficulty: difficult

"""
思路：

每个位置上积水的高度，应该等于min（左边最高的柱子高度，右边最高的柱子高度） -  这个位置上的柱子高度。

所以先从左往右遍历把left_max数组生成，left_max[i]代表 height[i] 及其左侧最高的柱子高度。

同理生成right_max。

然后再遍历一次对于每个位置计算min(left_max[i], right_max[i]) - height[i]就好了

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0 for _ in height]
        right_max = [0 for _ in height]
        water = [0 for _ in height]

        for i in range(len(height)):
            if i > 0:
                left_max[i] = max(left_max[i-1],height[i])
            else:
                left_max[i] = height[i]

        for i in range(len(height)-1,-1,-1):
            if i < len(height) - 1:
                right_max[i] = max(right_max[i+1],height[i])
            else:
                right_max[i] = height[i]

        for i in range(len(height)):
            tmp = min(left_max[i],right_max[i]) - height[i]
            if tmp > 0:
                water[i] = tmp

        return sum(water)


