#label: string difficulty: easy

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        """
        解题思路：
        等价字符串实际就是如果字符串的奇数位都一样则字符串等价，或者偶数位都一样字符串等价
        只需找到字符串的奇偶数位保存排序即可
        """
        n = len(A)
        tmp = set()
        for st in A:
            s1="" #保存字符串的奇数位
            s2="" #保存字符串的偶数位
            for i in range(len(st)):
                if i%2 == 1:
                    s1 += st[i]
                else:
                    s2 += st[i]
            s1 = list(s1)
            s2 = list(s2)
            s1.sort()
            s2.sort()
            s1 = "".join(s1)
            s2 = "".join(s2)
            tmp.add(s1+s2)
            
        return len(tmp)
