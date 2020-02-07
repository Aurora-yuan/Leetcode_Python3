#label: hashmap difficulty: medium

"""
第一种思路：

线性扫描一遍S，把所有的长度为10的子串找出来，用hashmap记录出现的次数。

然后输出出现次数 > 1 的子串。

"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import defaultdict
        n = len(s)
        lookup = defaultdict(int)
        for i in range(0,n-9):
            lookup[s[i:i+10]] += 1
        return [key for key,value in lookup.items() if value> 1]

"""
第二种思路：

声明两个set, seen表示目前出现过的子串，repeat表示目前重复出现过的子串。

线性扫描S里所有长度为10的子串，如果该子串没有在seen里出现过，就把它塞进去；如果出现过了，就说明它重复出现了，放到repeat里。

最后返回repeat的列表形式即可。

"""

class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen, repeat = set(), set()
        for i in range(len(s) - 9):
            temp = s[i:i + 10]
            if temp in seen:
                repeat.add(temp)
            else:
                seen.add(temp)
                
        return list(repeat)


