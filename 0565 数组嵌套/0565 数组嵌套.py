#label: array difficulty: medium

"""
思路：

官方解法

"""

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # 官方解法一：暴力法(超出时间限制)
        # def checklen(index):
        #     checkset = set()
        #     while True:
        #         checkset.add(index)
        #         if nums[index] not in checkset:
        #             index = nums[index]
        #         else:
        #             break
        #     return len(checkset)

        # ans = 0
        # for i in nums:
        #     ans = max(ans,checklen(i))
        # return ans

        # 官方解法二
        def checklen(index):
            checkset = set()
            while True:
                visited[index] = 1
                checkset.add(index)
                if nums[index] not in checkset:
                    index = nums[index]
                else:
                    break
            return len(checkset)

        ans = 0
        visited = [0] * len(nums)
        for i in nums:
            if visited[i] != 1:
                ans = max(ans,checklen(i))

        return ans

