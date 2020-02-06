#label: 链表 difficulty: medium

"""
思路：

链表问题上递归。

每次递归就只考虑交换第一个和第二个节点，

basecase是如果只有0个或1个节点，那么不用交换，直接返回head，

用两个指针first和second分别指向需要进行交换的两个节点，

然后一通操作保证它们交换即可。

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node1,node2 = head, head.next
        tmp = self.swapPairs(node2.next)
        node2.next = node1
        node1.next = tmp
        return node2
        
        
"""
非递归的版本

"""

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            node1, node2 = pre.next, pre.next.next
            pre.next, node1.next = node2, node2.next
            node2.next = node1
            pre = node1
        return dummy.next



