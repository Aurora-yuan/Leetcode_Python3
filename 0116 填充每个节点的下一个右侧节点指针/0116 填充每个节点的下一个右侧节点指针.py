#label: tree difficulty: medium

"""
第一种思路：

如果不要求O(1)的空间复杂度，那么可以利用层序遍历得到每个节点的next指针指向的节点……

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = [root]
        while(queue):
            next_queue = []
            
            for i, node in enumerate(queue):
                if not node:
                    continue
                if i != len(queue) - 1:#不是最后一个
                    node.next = queue[i + 1]
                else:
                    node.next = None
                next_queue.append(node.left)
                next_queue.append(node.right)
            queue = next_queue[:]
        
        return root

"""

思路：

既然要求了O(1)的空间复杂度，那么就得换一种思路：

观察可得，对于每个节点Node的左孩子Node.left，这个左孩子的next一定是指向它的兄弟节点，即Node.right

对于每个节点Node的右孩子，就得分两种情况讨论：

如果Node.next == None，即Node自己就没有下一个节点，那么Node.right也没有下一个节点。

如果Node有下一个节点, 那么Node.right.next = N

"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        #先排除掉不需要处理的情况
        if not root or (not root.left and not root.right):
            return root
        
        #某一个节点的左孩子的next一定是指向这个节点的右孩子
        root.left.next = root.right
        
        #当某一个节点的next不为空的时候，这个节点的右孩子的next一定是指向该节点next的left
        if root.next:
            root.right.next = root.next.left
        
        #递归处理下一层
        self.connect(root.left)
        self.connect(root.right)
  
        return root


