#label: tree difficulty: easy

"""
解题思路：

递归。主要在于理清其中的逻辑关系。

当合并的两个结点都是叶子节点时，最容易，逻辑取或即可。

只有其中一个结点是叶子节点时，如果叶子节点val=false，返回另一个结点。若这个叶子节点val=true，返回叶子节点。

如果两个结点都不是叶子，那么，递归的合并它们的4个孩子，一定要对应。如果合并以后，4个孩子都是叶子，并且它们的val相等，那么4个孩子合并，

逻辑值val与孩子相同，当前的结点设置为叶子。

"""

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            if quadTree1.val:
                return quadTree1
            else:
                return quadTree2
            
        if quadTree2.isLeaf:
            if quadTree2.val:
                return quadTree2
            else:
                return quadTree1
            
        topleft = self.intersect(quadTree1.topLeft,quadTree2.topLeft)
        topright = self.intersect(quadTree1.topRight,quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft,quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight,quadTree2.bottomRight)
        
        if topleft.isLeaf and topright.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topleft.val and topright.val and bottomLeft.val and bottomRight.val:
            return Node(True,True,None,None,None,None)
        else:
            return Node(False,False,topleft,topright,bottomLeft,bottomRight)




