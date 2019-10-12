#label: string difficulty: easy

"""
想求得0和1的个数相等的子串，数一下，连续的0,1的个数有多少，构成一个数组找出相邻的两个个数的最小值就好了。

比如“0001111”, 结果是min(3, 4) = 3, 即，(“01”, “0011”, “000111”)。

先统计连续的0和1分别有多少个，如：111100011000，得到4323；在4323中的任意相邻两个数字，取小的一个加起来，就是3+2+2 = 7.

"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l = [1]
        count = 0
        #对字符串中的0和1进行计数
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                l[-1] += 1
            elif s[i]!=s[i-1]:
                l.append(1)
        #每次取相邻的01串，根据0和1的长度计算子串个数
        for j in range(1,len(l)):
            num = min(l[j-1],l[j])
            count += num
        return count

