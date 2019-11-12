#label: DFS difficulty: easy

"""
思路：

先中序遍历给定树，然后根据中序遍历的结果构建题目要求的树即可。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        preorder = list()
        
        def pre_order(root):
            if not root:
                return
            pre_order(root.left)
            preorder.append(root.val)
            pre_order(root.right)
        
        pre_order(root)
        dummy = TreeNode(0)  #构建一个假的根结点，便于return
        for i, node in enumerate(preorder):
 
            temp = TreeNode(node)
            temp.left = None
            temp.right = None
            if i == 0:
                dummy.right = temp
                cur = temp
            else:
                cur.right = temp
                cur = temp
        return dummy.right


