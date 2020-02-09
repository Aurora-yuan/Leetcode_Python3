#label: tree difficulty: medium

"""

思路：

递归，分类讨论：

当一个Node既有左孩子又有右孩子的时候，显然左孩子的next就是右孩子，右孩子的next得在Node的next里往右找，直到某个节点有孩子，

这个孩子就是Node.right的next。

当一个Node只有左孩子的时候，左孩子的next得在Node的next里往右找。

当一个Node只有右孩子的时候，右孩子的next得在Node的next里往右找。

所以不妨用一个辅助函数findCousin(node, parent)来找到node.next，其中node是parent的子节点

对于一个需要找Cousin节点的node， 首先看叔叔节点parent.next有没有孩子，

如果有左孩子，那么很好这个左孩子就是结果，

如果没有左孩子但是有右孩子，那么也不错，这个右孩子是结果，

如果parent.next没有孩子，那么糟了，还得继续找更小的叔叔，即parent.next.next……

一直这么找下去，直到找到一个有孩子的叔叔，那么返回这个孩子，或者找完所有的叔叔，它们都没有孩子……

"""

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
        if not root or (not root.left and not root.right):
            return root
        
        def findCousin(node, parent):
            tmp = parent.next
            while(tmp):
                if tmp.left:
                    node.next = tmp.left
                    break
                    
                elif tmp.right:
                    node.next = tmp.right
                    break
                tmp = tmp.next
                
        if root.left and root.right:
            root.left.next = root.right
            findCousin(root.right, root)
            
        elif root.left:
            findCousin(root.left, root)
            
        elif root.right:
            findCousin(root.right, root)
        
        # print root.val, root.right.next
        self.connect(root.right)
        self.connect(root.left)
        
                
        return root


