#label: TREE difficulty: easy

"""
思路：

二叉树的直径等于 在 经过每个节点的最长路径里找最大值，

每个节点的最长路径的计算方法为 左右子树高度之和。

时间复杂度： O（N），因为每个节点遍历一次

空间复杂度： O（N）， 因为递归调用了Height（），需要花费递归栈的空间。平均开销是O（logN），但是当树退化为单链表的时候，就是O（N）。

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        def height(node):
            if not node:
                return 0
            left_h = height(node.left)
            right_h = height(node.right)
            
            self.res = max(self.res, left_h + right_h) 
            return 1 + max(left_h, right_h)
        
        height(root)
        return self.res

