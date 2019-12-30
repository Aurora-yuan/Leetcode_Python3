#label: dynamic programming difficulty: medium

"""
思路：

以每一个i都作一次根节点，i将数列分为两部分，（1，i-1）和（i+1, n)，在前一个区间中让每个j都做一次根节点构成的树作为i的左子树，

在后一个区间中让每个k都做一次根节点构成的树作为i的右子树，将所有的情况组合起来

来回只用到一个函数用来生成以i为根节点的树，递归调用即可，结束的条件就是没有节点可以生成，返回[None]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        def generate(start, end):
            trees = []
            for root in range(start, end):
                for left in generate(start, root):
                    for right in generate(root+1, end):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)
              
            return trees or [None]
        return generate(1,n+1)
