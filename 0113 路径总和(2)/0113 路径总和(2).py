#label: tree/dfs difficulty: medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        res = []
        def dfs(node,tmp):
            if not node:
                return
            tmp.append(node.val)
            if not node.left and not node.right and sum(tmp) == s:
                res.append(tmp[:])
            
            dfs(node.left,tmp)
            dfs(node.right,tmp)
            
            tmp.pop()
            
        dfs(root,list())
        return res
