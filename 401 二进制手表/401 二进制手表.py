class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ans = []
        for i in range(0,12):
            for j in range(0,60):
                if (bin(i) + bin(j)).count("1") == num:
                    ans.append("%d:%02d" % (i,j))
        return ans
