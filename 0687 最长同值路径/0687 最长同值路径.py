#label: recursive difficulty: easy

"""
类似问题

Leetcode 124：二叉树中的最大路径和（超详细的解法！！！）

Leetcode 543：二叉树的直径（超详细的解法！！！）

我们定义函数longestUnivalue返回左右两边其中最大的路径长度，此时我们有四种情况考虑

root.left == root == root.right
root.left == root
root.right == root
root.left ！= root != root.right
对于第一种情况此时左右孩子和根相同，我们需要更新我们的最大长度res=max(res,l+r+2)，并且返回max(l,r)+1。

对于第二种情况，此时左孩子和根相同，我们需要更新我们的最大长度res=max(res,l+1)，并且返回l+1。

对于第三种情况，此时右孩子和根相同，我们需要更新我们的最大长度res=max(res,r+1)，并且返回r+1。

对于第四种情况，此时只需返回0即可。

"""

class Solution:
    def longestUnivaluePath(self, root: 'TreeNode') -> 'int':
        res = 0
        def longestUnivalue(root):
            nonlocal res
            if not root:
                return 0
            l = longestUnivalue(root.left)
            r = longestUnivalue(root.right)
            if root.left and root.right and root.left.val == root.val == root.right.val:
                res = max(res, l + r + 2)
                return max(l, r) + 1
            elif root.left and root.left.val == root.val:
                res = max(res, l+1)
                return l + 1
            elif root.right and root.right.val == root.val:
                res = max(res, r+1)
                return r + 1
            else:
                return 0
            
        longestUnivalue(root)
        return res

#稍微简化一下上面的代码

class Solution:
    def longestUnivaluePath(self, root: 'TreeNode') -> 'int':
        res = 0
        def longestUnivalue(root):
            nonlocal res
            if not root:
                return 0
            l = longestUnivalue(root.left)
            r = longestUnivalue(root.right)
            pl, pr = 0, 0
            if root.left and root.left.val == root.val:
                pl = l + 1
            if root.right and root.right.val == root.val:
                pr = r + 1
            res = max(res, pl + pr)
            return max(pl, pr)
            
        longestUnivalue(root)
        return res

