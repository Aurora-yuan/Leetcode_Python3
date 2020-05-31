#label: 递归/dfs difficulty: difficult

"""
思路：

见https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/er-cha-shu-zui-da-lu-jing-he-qiu-shu-de-zui-chang-/

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
class Solution:
    def dfs_sum(self, root: TreeNode):
        if root == None: 
            return 0
        val = root.val
        sum_l = max(0, self.dfs_sum(root.left))
        sum_r = max(0, self.dfs_sum(root.right))
        self.ans = max(self.ans, sum_l + sum_r + val)
        return  max(sum_l, sum_r) + val
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = - 1e9
        self.dfs_sum(root)
        return self.ans
