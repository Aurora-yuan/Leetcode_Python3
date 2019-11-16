#label: TREE difficulty: easy

"""
思路：

递归，注意备份一下root.left 和root.right，因为会被覆盖

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left = root.left
        right = root.right
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)
        
        return root
