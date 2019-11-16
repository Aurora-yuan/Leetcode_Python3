#label: TREE difficulty: easy

"""
思路：

利用BST中序遍历为升序的性质找。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        res = 99999999
        l = inorder(root)
        for i in range(1,len(l)):
            res = min(res, l[i] - l[i-1])
        
        return res
        
