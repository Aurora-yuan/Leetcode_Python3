#label: TREE difficulty: easy

"""
思路：

直接按照右中左的顺序中序遍历整棵树，

用一个变量s记录下需要加的值。

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #右中左的遍历顺序
        if not root:
            return root
        self.s = 0
        
        def convert(node):
            if not node:
                return 
            
            convert(node.right)
            node.val += self.s
            self.s = node.val
            convert(node.left)
            
        convert(root)
        return root

