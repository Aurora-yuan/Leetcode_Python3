#label: tree difficulty: easy

"""
思路：

基础题，DFS+回溯找到每一条从根节点到叶节点的Path，存在res里，

然后线性扫描res这个数组，把每一条path利用int（BIN，2）函数转成十进制，再加到rres中。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = []
        
        def dfs(root,tmp):
            if not root:
                return
            tmp += str(root.val)
            if not root.left and not root.right:
                res.append(tmp[:])
                
            dfs(root.left,tmp)
            dfs(root.right,tmp)
            
            tmp = tmp[:-1]
            
        dfs(root,"")
        rres = 0
        for item in res:
            rres += int(item,2)
            rres %= (10**9+7)
            
        return rres
