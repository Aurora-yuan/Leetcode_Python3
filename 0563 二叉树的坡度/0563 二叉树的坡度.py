#label: tree difficulty: easy

"""
思路

既然是二叉树的遍历问题，那想必是递归了。再看对于某个结点，需要先得到左子树和右子树的和，才能计算tilt，那就是后序遍历了，模板就是：

def sum_and_tilt(root):
    ...
    sum_left, tilt_left = sum_and_tilt(root.left)
    sum_right, tilt_right = sum_and_tilt(root.right)
    # TODO
    return sum,tilt
    
下面来考虑sum和tilt该如何计算。sum即以当前结点为根节点的所有结点的和，那就是sum_left + sum_right + root.value了。

当前结点的tilt是左子树结点和与右子树结点和的差，那就是abs(sum_left - sum_right)；注意这里返回的tilt是包括其左右子树的tilt的，

所以最终就是abs(sum_left - sum_right) + tilt_left + tilt_right。

再仔细考虑tilt，实际上tilt不必要放在递归结构中返回，直接让tilt作为成员变量，保存累加和就好了，这样也避免和很多语言不支持return多个变量的问题。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def sum_and_tilt(root):
            if not root:
                return 0,0
            sum_left,tilt_left = sum_and_tilt(root.left)
            sum_right,tilt_right = sum_and_tilt(root.right)
            return sum_left+sum_right+root.val,abs(sum_left-sum_right)+tilt_left+tilt_right
    
        sum_tree,tilt_tree = sum_and_tilt(root)
        
        return tilt_tree
