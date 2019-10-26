#label: 链表 difficulty: easy

"""
思路：

跟传统的 从链表里删除一个节点（给定head和要删除的node） 不同，这一题只给出了要删除的node， 所以有所差异。

因为题目给了一些说明来限定条件：

最关键的在于给定的节点为非末尾节点而且必定有效，

所以就可以用node.next的值覆盖node的值，然后把node.next这个节点删除。

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
