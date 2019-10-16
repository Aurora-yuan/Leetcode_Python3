#label: 双指针/链表 difficulty: easy

"""
第一种思路：

哈希表，

线性扫描整个链表

把每个访问过的节点都放进哈希表里，

如果发现当前节点已经在表内，则说明链表有环。

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        record = dict()
        p = head
        while p:
            if p not in record:
                record[p] = 1
            else:
                return True
            p = p.next
        return False
        
 """
 第二种思路：

快慢指针法，快指针一次走两步，慢指针一次走一步，如果快慢指针相遇，则说明链表有环。
 """
 
 class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow, fast = head, head
        
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            if slow == fast:
                return True
        return False

