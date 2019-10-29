#label: array difficulty: easy

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #实际上就是问现在的数组和排序后的数组有几个位置的不同
        count = 0
        right = sorted(heights)
        for i in range(len(heights)):
            if right[i] != heights[i]:
                count += 1
        return count
