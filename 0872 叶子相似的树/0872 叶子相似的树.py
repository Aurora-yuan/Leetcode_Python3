#label: DFS difficulty: easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        #将两颗树的叶值序列找出来，比较即可。利用DFS寻找树的叶值序列
        leaf1,leaf2 = list(),list()
        
        def dfs(node,leaf):
            if not node:
                return
            if not node.left and not node.right:
                leaf.append(node.val)
                return
            dfs(node.left,leaf)
            dfs(node.right,leaf)
        
        dfs(root1,leaf1)
        dfs(root2,leaf2)
        
        return leaf1 == leaf2
