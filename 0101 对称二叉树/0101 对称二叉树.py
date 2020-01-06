#label: tree difficulty: medium

"""
第一种思路：

层序遍历找出来，判断每一层是不是回文数组。

注意：跟普通的层序遍历不一样的地方在于：如果是空结点，也要把None添加到层序遍历的结果数组里。

"""

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        queue = [root]
        
        while(queue):
            next_queue = list()
            layer = list()
            for node in queue:
                if not node:
                    layer.append(None)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)
                
                layer.append(node.val)
                
            if layer != layer[::-1]:
                return False
            queue = next_queue
            
        return True

"""
第二种思路：

递归，核心思想就是两个node一左一右地对比是不是一样。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(node1,node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            
            return check(node1.right,node2.left) and check(node1.left,node2.right)
        
        return check(root,root)
