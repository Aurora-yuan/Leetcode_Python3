#label: array difficulty: easy

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        length = len(seats)
        turn = []
        # 把有人坐的座位下标提出来
        for i in range(length):
            if seats[i] == 1:
                turn.append(i)
        # 考虑最左最右是零的情况
        ans = max(turn[0], length-turn[-1]-1)
        # 离他最近的人的最大距离即相邻有人坐的座位之间距离的一半
        for i in range(0, len(turn)-1):
            if (turn[i+1] - turn[i])/2 > ans:
                ans = (turn[i+1] - turn[i]) / 2
        return ans


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # 从前往后：计算当前位置距离最近1的位置
        # 从后往前：计算当前位置距离最近1的位置
        if not seats:
            return None
        dp = [0]*len(seats)
        cur = seats.index(1)
        for i in range(len(seats)):
            if seats[i] == 1:
                cur = i
            dp[i] = abs(i - cur)
        #经过前向遍历后，cur已经指向了最后一个为1的元素
        for i in range(len(seats)-1,-1,-1):
            if seats[i] == 1:
                cur = i
            dp[i] = min(abs(cur - i), dp[i])
        # print(dp)
        return max(dp)

