#label: tree difficulty: easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        #遍历二叉树，和根结点的值不符则返回False
        self.value = root.val
        self.result = True
        self.generate(root)
        
        return self.result
    
    def generate(self,root):
        if self.value != root.val:
            self.result = False
            return
        if not root:
            return
        if root.left:
            self.generate(root.left)
        if root.right:
            self.generate(root.right)
            
