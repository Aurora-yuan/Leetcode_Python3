#label: tree difficulty: medium

"""
思路：

二叉搜索树的条件就是root.left<root<root.right，不就是要求中序遍历严格升序吗？
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        res = inorder(root)
        return len(res) == len(set(res)) and res == sorted(res)
