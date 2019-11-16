#label: TREE difficulty: easy

"""
首先解读题干，题干的要求是找和为sum的路径总数，这次路径的起点和终点不要求是根结点和叶结点，可以是任意起终点，而且结点的数值有正有负，

但是要求不能回溯，只能是从父结点到子结点的。在已经做了路径总和一和二的基础上，我们用一个全局变量来保存路径总数量，在主调函数中定义变量self.result=0。
因为数值有正有负，所以在当我们找到一条路径和已经等于sum的时候，不能停止对这条路径的递归，因为下面的结点可能加加减减，

再次出现路径和为sum的情况，因此当遇到和为sum的情况时，只需要用self.result+=1把这条路径记住，然后继续向下进行即可。即下面这段代码：
sum1+=root.val
    if sum1==sum:
        self.result+=1
    if root.left:
        self.dfs(root.left,sum1,sum)
    if root.right:
        self.dfs(root.right,sum1,sum)
        
由于路径的起点不一定是根结点，所以需要对这棵树的所有结点都执行一次搜索，就是树的遍历问题，每到一个结点就执行一次dfs去搜索以该结点为起点的路径：
def search(self,root,sum):
    if not root: return 
    self.dfs(root,0,sum)
    self.search(root.left,sum)
    self.search(root.right,sum)
在主调函数中，调用search()函数，search函数实现树的遍历。

在search函数中，调用dfs函数，dfs函数实现以某结点为根结点的路径的查找。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.result=0
        self.search(root,sum)
        return self.result
    def search(self,root,sum):
        if not root: return 
        self.dfs(root,0,sum)
        self.search(root.left,sum)
        self.search(root.right,sum)
        
    def dfs(self,root,sum1,sum):
        if not root:return
        sum1+=root.val
        if sum1==sum:
            self.result+=1
        if root.left:
            self.dfs(root.left,sum1,sum)
        if root.right:
            self.dfs(root.right,sum1,sum)


