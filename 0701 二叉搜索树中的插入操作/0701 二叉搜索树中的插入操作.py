# label: BST difficulty: medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 方法一：递归，找到一个可以插入的位置
        # if not root:
        #     return TreeNode(val)
        # if root.val < val:
        #     root.right = self.insertIntoBST(root.right,val)
        # elif root.val > val:
        #     root.left = self.insertIntoBST(root.left,val)

        # return root

        # 方法二：迭代，找到插入后节点的父节点
        if not root:
            return TreeNode(val)
        node,parent = root,root
        while node:
            parent = node
            node = parent.left if val < parent.val else parent.right
        if val > parent.val:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)

        return root
