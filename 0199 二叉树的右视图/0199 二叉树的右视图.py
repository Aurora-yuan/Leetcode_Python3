#label: tree difficulty: medium

"""
第一种思路：

先把二叉树的层序遍历搞定，然后把每一层最后一个加入到result里即可。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        queue = [root]
        res = []
        while queue:
            next_queue = []
            layer = []
            for node in queue:
                if node:
                    layer.append(node.val)
                    next_queue += [node.left,node.right]
            queue = next_queue[:]
            if layer:
                res.append(layer[-1])
            
        return res
        
“”“
第二种思路：

DFS搜索，先右子树再左子树的搜索顺序，这样保障每一层搜索到的第一个节点都是最右的节点，

当搜索到新的一层时，就把第一个有效节点放到答案里。
 
”“”

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(node, depth):
            if not node:
                return
            if depth > len(res):
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth +1)
            
            
        dfs(root, 1)
        return res

