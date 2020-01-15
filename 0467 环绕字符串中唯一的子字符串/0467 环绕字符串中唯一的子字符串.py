#label: dynamic programming difficulty: medium

"""
思路

问题可以转化为，对于每一个字母，求出它们前置连续最长子串长度，对每个字母的前置连续最长子串长度求和。
因为每一个字母的前置子串，在前置子串长度一定时，那么它的子串是唯一的。
如'zab'，'z'的前置最长连续子串长度为1， 'a'为2， 'b'为3，再统计它们的和

"""

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p: 
            return 0
        N = len(p)
        arr = [0] * 128 #保存前置连续最长字串的长度的数组
        arr[ord(p[0])] = 1#初始化第一个字母长度为1
        prelen = 1#保存前置长度的临时变量
        for i in range(1, N):
            m = ord(p[i]) - ord(p[i-1])
            if m == 1 or m == -25:#前后字母连续
                prelen += 1  #连续则加1
            else:
                prelen = 1 #不连续重置为1
            arr[ord(p[i])] = max(prelen, arr[ord(p[i])])
        return sum(arr)

