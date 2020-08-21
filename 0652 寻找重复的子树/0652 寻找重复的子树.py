# label: dfs + hashmap difficulty: medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        # 使用字典 d 记录｛子树结构：[root1，root2，……]｝
        d = collections.defaultdict(list)
        def dfs(root):
            if not root: return ''
            s = ' '.join((str(root.val), dfs(root.left), dfs(root.right)))
            d[s].append(root)
            return s
        dfs(root)
        return [l[0] for l in d.values() if len(l) > 1]
