#label: 贪心算法 difficulty: medium

"""
思路

1.排序：按照身高从高到低排，升高相同的按k从小到大排
2.插入：按照排序好的顺序逐个插入新数组，插入的位置按照k来插

如示例中，排序完：
[[7,0], [7,1], [6,1], [5,0], [5,2]，[4,4]]
插入的过程：
第一插：[[7,0]]
第二插：[[7,0], [7,1]]
第三插：[[7,0], [6,1],[7,1]]
第四插：[[5,0],[7,0], [6,1],[7,1]]
...
先插高的，后插矮的，即使后插的插到前面也不会有影像，因为矮

"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda (h, k): (-h, k))
        res = []
        for p in people:
             
            res.insert(p[1],p)
        return res
