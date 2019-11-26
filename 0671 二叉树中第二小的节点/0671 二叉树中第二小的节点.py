#label: tree difficulty: easy

"""
思路：

根据题意，每条从根节点向下的path一定是非递减序列，

所以可以把每条path上第一个不等于root.val的值存到数组res里，

然后排序res，如果有答案就返回res[0]，没有就返回-1。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = []
        
        def dfs(node):
            if not node:
                return
            if node.val != root.val:
                res.append(node.val)
                return
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        res.sort()
        return -1 if len(res) == 0 else res[0]
