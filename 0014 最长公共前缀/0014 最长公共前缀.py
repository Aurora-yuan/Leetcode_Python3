#label: string difficulty: easy

"""
思路一：

调用python库
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return os.path.commonprefix(strs)


"""
思路二：

首先找到最短的那个字符串，因为最长前缀不会超过这个最短字符串的长度。然后将该字符串转换为枚举对象，一旦比对不成功，则返回当前最长的前缀

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #判断是否为空
        if not strs:
            return ""

        # 找到最短的字符串
        shortest = min(strs, key=len)

        # 转换为枚举对象
        for i_th, letter in enumerate(shortest):
            for other in strs:
                if other[i_th] != letter:
                    return shortest[:i_th]

        return shortest
