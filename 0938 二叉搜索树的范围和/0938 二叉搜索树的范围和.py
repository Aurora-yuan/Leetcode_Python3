#label: recursive difficulty: easy

"""
思路一：

中序遍历，直接把所有节点找出来

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.res = 0
        
        #中序遍历
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            if node.val >= L and node.val <= R:
                self.res += node.val
            inorder(node.right)
            
        inorder(root)
        return self.res 


“”“”
思路二：

利用BST的性质递归。

先处理根节点，

然后判断一下要不要在右子树里找，

如果根节点的值都比R大了，那么右子树里的节点只会更大，就不用在右子树里找了，

所以在右子树里找的条件是root.val < R。

左子树同理。

“”“”

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        
        if not root:
            return 0
        if L <= root.val <= R:
            res += root.val
        if root.val < R:
            res += self.rangeSumBST(root.right, L, R)
        if root.val > L:
            res += self.rangeSumBST(root.left, L, R)
            
        return res

