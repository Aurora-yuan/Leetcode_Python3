#label: TREE difficulty: easy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        else:
            res = []
            self.middle_digui(root, res)
        from collections import Counter
        dic = Counter(res)
        max = 0
        for k in dic:
            if dic[k] > max:
                max = dic[k]
        temp = []
        for k in dic:
            if dic[k] == max:
                temp.append(k)
        return temp
 
 
    def middle_digui(self,root,res):
        if root == None:
            return
        self.middle_digui(root.left,res)
        res.append(root.val)
        self.middle_digui(root.right,res)

