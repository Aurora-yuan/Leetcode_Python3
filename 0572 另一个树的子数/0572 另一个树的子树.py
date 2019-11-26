#label: tree difficulty: easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# 定义函数判断两棵树是否相等
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return False
        # 借助队列来实现树的层次遍历
        queue = [s]
        while queue:
            temp = queue.pop(0)
            # 访问每个节点，看当前节点及子孙是否满足要求
            flag = self.isSameTree(temp, t)
            if flag:
                return True
            else:
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            
        return False


