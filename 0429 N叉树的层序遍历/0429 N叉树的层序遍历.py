#label: tree difficulty: medium

"""
思路：

和二叉树的层序遍历思路一致，只不过把node.left和node.right改成node.children

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            next_queue = []
            layer = []
            for node in queue:
                if node:
                    layer.append(node.val)
                    for child in node.children:
                        next_queue.append(child)
            queue = next_queue[:]
            if layer:
                res.append(layer)
        return res
