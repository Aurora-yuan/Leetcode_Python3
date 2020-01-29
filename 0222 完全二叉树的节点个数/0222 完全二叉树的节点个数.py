#label: tree difficulty: medium

"""
第一种思路：

按照处理树相关问题的经验，

先处理根节点，再递归地处理左右子树。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        
"""
第二种思路：

随便一种遍历方法统计即可，中序前序后序层序。

"""

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = []
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            self.res.append(node.val)
            inorder(node.right)
            
        inorder(root)
        return len(self.res)

