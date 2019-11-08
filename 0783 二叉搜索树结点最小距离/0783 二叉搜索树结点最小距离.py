#label: recursive difficulty: easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        #利用BST中序遍历为升序的性质找
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        res = 999999
        l = inorder(root)
        for i in range(1, len(l)):
            res = min(res, l[i] - l[i - 1])
            
        return res

