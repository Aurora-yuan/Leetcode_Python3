#label: tree difficulty: medium

"""
思路：

递归，如果当前节点就是p或q，说明当前节点就是最近的祖先，

如果当前节点不是p或p，就试着从左右子树里找pq。

如果pq分别在一左一右被找到，那么当前节点还是最近的祖先返回root就好了，

否则，返回它们都在的那一边。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            
            if left and right: #一个在左子树，一个在右子树
                return root
            elif left:#都在左子树
                return left
            elif right:#都在右子树
                return right
            else:
                return
 


