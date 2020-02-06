#label: link difficulty: medium

"""
思路：

快慢指针法。先判断链表有没有环，

如果链表有环，则让快指针回到链表的头重新出发，

当快慢指针相遇的那个节点即是链表环的起点。

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
                
            if slow == fast:
                break
        if slow != fast: #链表无环
            return None
        
        fast = head
        while slow:
            if slow == fast: #此点即是环起点
                return slow
            slow = slow.next
            fast = fast.next


