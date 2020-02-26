#lable: 双指针 difficulty: medium

"""
思路：

问子串可以考虑用双指针法 +  sliding window解题，start， end可以夹出一个window。

用end线性遍历每个数组，用record记录下每个字母出现的最新的下标。

当遇到一个新元素char在record里没有记录时，代表它没有跟window里的字母重复。

如果在record里有记录，说明start需要刷新， 取当前start和record[char]里的最大值作为新的start即可。

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = dict()#记录每个字母最后一次出现的下标,key是字母，val是下标
        res, start = 0, 0
        for end in range(len(s)):
            if s[end] in record:#出现过
                start = max(start, record[s[end]] + 1)
            record[s[end]] = end #刷新最新下标
            res = max(res, end - start + 1)  #刷新res        
        return res
