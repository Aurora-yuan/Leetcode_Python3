#label: tree difficulty: medium

"""

思路：

利用BST的性质：BST的中序遍历为升序数组。

所以直接在init里用中序遍历然后存进数组里就好了

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.res = list()
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.res.append(node.val)
            inorder(node.right)
            
        inorder(root)
        self.index = 0

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.res[self.index - 1]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index < len(self.res)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
