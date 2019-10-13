#label: string difficulty: easy

"""
Solution:(设置三个指针对字符串进行切片操作[由于索引超出字符串范围的切片得到的是空字符串或空列表，所以不影响结果])
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left, mid, right = 0, k, 2*k
        res = ''
        
        while len(res) < len(s):
            res += s[left:mid][::-1] + s[mid:right]
            left, mid, right = left + 2*k, mid + 2*k, right + 2*k
        return res

