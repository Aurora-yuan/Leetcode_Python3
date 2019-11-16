#label: TREE difficulty: easy

"""
思路：

当处理到一个node时，如果它的左孩子是叶子，就返回左孩子的值加上右子树调用这个函数的结果，

如果它的左孩子不是叶子，就返回左右子树调用这个函数的结果的和。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left:
            if not root.left.left and not root.left.right:
                return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


