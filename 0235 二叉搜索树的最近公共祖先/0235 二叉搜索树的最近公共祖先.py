#label: TREE difficulty: easy

"""
第一种思路：

先把从根节点分别到P和Q的路径找出来，然后找两条路径上相同的最后一个节点就是P和Q的最近公共祖先。

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        p_path = list()
        q_path = list()
        self.findPath(root, p, p_path)
        self.findPath(root, q, q_path)
        
        # for node in range(len(p_path)):
        #     print p_path[node].val
        # for node in range(len(q_path)):
        #     print q_path[node].val
        
        l = min(len(p_path), len(q_path))
        
        for node in range(l):
            if p_path[node].val != q_path[node].val:
                break
                
        if p_path[node].val == q_path[node].val:    
            return p_path[node]
        else:
            return p_path[node - 1]
        
    def findPath(self, root, node, path):
        if not root:
            return None
        
        path.append(root)
        
        if root.val == node.val:
            return 
        if root.val > node.val:
            self.findPath(root.left, node, path)
        if root.val < node.val:
            self.findPath(root.right, node, path)
        
        return


"""

第二种思路：

利用二叉搜索树的性质找。

左子树的所有节点的值都比根节点的值要小， 右子树所有节点的值都比根节点的值要大。

根据这条性质就可以判断P, Q是在根节点的左边还是右边。

"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (root.val - p.val) * (root.val - q.val) <= 0: # p, q一左一右
            return root
        elif root.val > p.val: # p, q 都在左边
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val: # p, q 都在右边
            return self.lowestCommonAncestor(root.right, p, q)


