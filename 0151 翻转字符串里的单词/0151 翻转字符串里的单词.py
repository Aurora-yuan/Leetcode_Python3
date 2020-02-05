#label: string difficulty: medium

"""
思路：

先用rstrip和lstrip把字符串开头和结尾所有多出来的空格去掉。

然后用split把所有的单词切割出来，注意可能会切出来空字符串。

翻转一下，然后把所有的单词join在一起就好啦！

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.lstrip()
        s = s.rstrip()
        l = s.split(' ')
        l = l[::-1]
        return ' '.join(item for item in l if item != '')
