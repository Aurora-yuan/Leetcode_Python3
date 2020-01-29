#label: tree difficulty: medium

"""
思路：

二叉搜索树的中序遍历就是把所有节点的值按从小到大的顺序排列的，

所以只需要找出中序遍历数组result，然后返回result[k-1]即可。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorderTraversal(node):
            if not node:
                return []
            return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)
        
        l = inorderTraversal(root)
        return l[k - 1]


