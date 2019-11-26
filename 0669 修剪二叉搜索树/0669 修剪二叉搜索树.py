#label: tree difficulty: easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        if root.val >= L and root.val <=R:
            root.left = self.trimBST(root.left,L,R)
            root.right = self.trimBST(root.right,L,R)
            return root
        
        if root.val < L:
            return self.trimBST(root.right,L,R)
        
        if root.val > R:
            return self.trimBST(root.left,L,R)
