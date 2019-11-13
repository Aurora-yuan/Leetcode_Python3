#label: DFS difficulty: easy

"""
对于每个node，都判断一下其左右子树的相对高度，然后根据相对高度判断这个node满不满足条件，

再递归地判断其左右孩子满不满足条件。

这种思路会重复计算高度，所以会慢。

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        
        def getHeight(node, h):
            if not node:
                return h
            h += 1
            return max(getHeight(node.left, h),getHeight(node.right, h))
 
        
        l_height = getHeight(root.left, 0)
        r_height = getHeight(root.right, 0)
        
        return abs(l_height - r_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


"""
如果每一步都计算树高，效率太低，故转变了思想。 递归判断每一个节点的均衡状态，并且只计算一次树高，直至根节点。

"""

class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        
        def check(root,height):
            if not root:
                return True,height
            
            tag1,height1=check(root.left,height+1)
            tag2,height2=check(root.right,height+1)
            if tag1 and tag2 and abs(height1-height2)<2:
                return True,max(height1,height2)
            else:
                return False,height1
            
        tag,height=check(root,0)
        return tag  

