#label: array difficulty: medium

"""
思路一：

初始化一个res数组全为0，如果某一时刻i，提莫攻击了艾希，则把res[i]到res[i + duration -1]之间全部置为1，

最后返回sum（res）即可，

这种思路的问题在于题目数据规模有点大，过不了OJ

"""

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        timeSeries.sort()
        res = [0] * 200000100
        for i in range(len(timeSeries)):
            for j in range(duration):
                res[timeSeries[i] + j] = 1
        return sum(res)

"""
思路二：

线性扫描，扫描到提莫攻击的每个时刻时，先判断一下下一次攻击时艾希还会不会处在中毒的状态，

如果艾希已经不再中毒，那么res 直接加上duration即可，

如果艾希还在中毒，那么res就加上两个时刻之差，代表中毒状态刷新，

最后记得加上最后一次射击带来的中毒持续时间（如果存在最后一次射击的话）。

"""

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        l = len(timeSeries)
        res = 0
        for i in range(l-1):
            if timeSeries[i] + duration <= timeSeries[i+1]:
                res += duration
            else:
                res += timeSeries[i+1] - timeSeries[i]

        return res + duration
