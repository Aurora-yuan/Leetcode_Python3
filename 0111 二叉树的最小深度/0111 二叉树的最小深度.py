#label: BFS difficulty: easy

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.depth_list = list()
        self.findAllDepth(root, 0)
        print self.depth_list
        return min(self.depth_list)
    
    def findAllDepth(self, node, depth):
        if not node.left and not node.right:
            depth += 1
            self.depth_list.append(depth)
            return
        if node.left:
            self.findAllDepth(node.left, depth + 1)
        if node.right:
            self.findAllDepth(node.right, depth + 1)
        return


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            if root.left and root.right:
                return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
            if root.left:
                return 1 + self.minDepth(root.left)
            if root.right:
                return 1 + self.minDepth(root.right)
            else:
                return 1
        else:
            return 0

