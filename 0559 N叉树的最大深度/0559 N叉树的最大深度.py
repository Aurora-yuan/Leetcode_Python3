#label: BFS difficulty: easy

"""
思路：

简单的递归就行了，

把root的所有孩子的分别的最大深度存在result这个数组里，最后返回1 + 这个数组的最大值，

需要注意max（）处理的数组必须不为空，所以最后返回时加了一个 if else做判断。

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        result = []
        if not root:
            return 0
        for node in root.children:
            result.append(self.maxDepth(node))
        
        return 1 + max(result) if result else 1

