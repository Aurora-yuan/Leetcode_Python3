#label: tree difficulty: easy

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = list()
        for leaf in root.children:
            res += self.postorder(leaf)
            
        return res + [root.val]
