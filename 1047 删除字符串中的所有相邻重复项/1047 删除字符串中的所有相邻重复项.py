#label: stack difficulty: easy

"""
思路一：

直接循环，空间复杂度低，但时间复杂度高

"""

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        flag = 1
        while 1:
            original_l = len(S)
            i = 0
            while i < len(S) - 1:
                if i >= 0 and S[i] == S[i + 1]:
                    S = S[:i] + S[i + 2:]
                    i -= 2
                i += 1 
            if original_l == len(S):
                return S

“”“
思路二：

我们可以用字符串自带的替换函数，由于字符串仅包含小写字母，因此只有 26 种不同的重复项。

将 aa 到 zz 的 26 种重复项放入集合中；

遍历这 26 种重复项，并用字符串的替换函数把重复项替换成空串。

注意，在进行过一次替换之后，可能会出现新的重复项。例如对于字符串 abbaca，如果替换了重复项 bb，字符串会变为 aaca，出现了新的重复项 aa。

因此，上面的过程需要背重复若干次，直到字符串在一整轮替换过程后保持不变（即长度不变）为止。

”“”

from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, S: str) -> str:
        # generate 26 possible duplicates
        duplicates = {2 * ch for ch in ascii_lowercase}
        
        prev_length = -1
        while prev_length != len(S):
            prev_length = len(S)
            for d in duplicates:
                S = S.replace(d, '')
                
        return S

“”“
思路三：

栈。我们可以用栈来维护没有重复项的字母序列：

若当前的字母和栈顶的字母相同，则弹出栈顶的字母；

若当前的字母和栈顶的字母不同，则放入当前的字母。

”“”

class Solution:
    def removeDuplicates(self, S: str) -> str:
        output = []
        for ch in S:
            if output and ch == output[-1]: 
                output.pop()
            else: 
                output.append(ch)
        return ''.join(output)
