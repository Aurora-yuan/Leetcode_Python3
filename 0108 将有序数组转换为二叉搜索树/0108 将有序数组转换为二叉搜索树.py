#label: DFS difficulty: easy

"""
思路：

输入数组已有序，相当于是BST的中序遍历，所以只要按照中序遍历的逆过程就可以建立BST了。

中序遍历数组的中间元素 nums[mid] 是root，

左子树是用nums[ :mid]建立的BST，右子树是用nums[mid + 1:]建立的BST。

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
             
        def dfs(start, end):
            if end < start:
                return 
            
            mid = (end + start) // 2
            root = TreeNode(nums[mid])
            
            root.left = dfs(start, mid - 1)
            root.right = dfs(mid + 1, end)
            
            return root
 
        return dfs(0, len(nums) - 1)



class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        l = len(nums)
        root = TreeNode(nums[l // 2])
        root.left = self.sortedArrayToBST(nums[:l//2])
        root.right = self.sortedArrayToBST(nums[l//2 + 1:])
        return root

