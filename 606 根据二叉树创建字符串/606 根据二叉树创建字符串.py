#label: 递归 difficulty: easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        res = ''
        if not t:
            return res
        res += str(t.val)
        if t.left:
            res += "("+self.tree2str(t.left) +")"
        else:
            if t.right:
                res += '()'
        if t.right:
            res += "("+self.tree2str(t.right) +")"
        return res

