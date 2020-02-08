#label: array/tree difficulty: medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]
        
        l_left = len(left_inorder)
        left_postorder = postorder[:l_left]
        right_postorder = postorder[l_left:-1]
        
        root.left = self.buildTree(left_inorder,left_postorder)
        root.right = self.buildTree(right_inorder,right_postorder)
        
        return root
