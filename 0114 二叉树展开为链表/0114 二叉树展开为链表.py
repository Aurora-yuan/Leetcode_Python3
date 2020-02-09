#label: tree difficulty: medium


"""
思路：

递归。先把左右子树捋直，然后备份右子树，把捋直的左子树移到右子树的位置上，把左子树置空，

找到现在右子树的末尾，把捋直的原来的右子树接上去。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return root
        
        #先把左右子树捋直
        self.flatten(root.left)
        self.flatten(root.right)
        
        tmp = root.right #把捋直的右子树备份一下
        
        root.right = root.left #把捋直的左子树放到右边
        root.left = None #记得把左子树置空
        while(root.right): #找到现在右子树的最后一个node
            root = root.right
        root.right = tmp #把捋直的原来的右子树接上去



