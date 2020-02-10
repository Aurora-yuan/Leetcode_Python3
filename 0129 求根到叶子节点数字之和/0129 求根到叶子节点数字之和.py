#label: tree/dfs difficulty: medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(node,tmp):
            if not node:
                return
            
            tmp = tmp * 10 + node.val
            if not node.left and not node.right:
                self.res += tmp
            
            dfs(node.left,tmp)
            dfs(node.right,tmp)
            
            tmp /= 10 # 回溯
            
        dfs(root,0)
        return self.res
