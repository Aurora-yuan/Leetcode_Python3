#label: recurrence difficulty: medium

"""
思路：

递归排序，

1. 找中点，把链表一分为二

2. 递归处理左右半边

3. 合并排好序的部分

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, slow, fast = head, head, head
        while fast and fast.next: #找链表中点,最终slow指向链表中点
            pre = slow
            slow = slow.next
            fast = fast.next.next
 
        pre.next = None
        left, right = self.sortList(head), self.sortList(slow)
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            head = ListNode(l1.val)
            head.next = self.merge(l1.next, l2)
        else:
            head = ListNode(l2.val)
            head.next = self.merge(l1, l2.next)
        return head


