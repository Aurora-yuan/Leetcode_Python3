#label: string difficulty: easy

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        #这题有些唬人，转换题意后很简单,实际就是比较两个字符串的长度
        if len(a) != len(b):
            return max(len(a),len(b))
        elif len(a) == len(b) and a == b:
            return -1
        else:
            return len(a)
