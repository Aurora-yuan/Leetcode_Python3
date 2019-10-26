#label: 链表 difficulty: easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newhead = ListNode(0)
        p = newhead
        while(l1 and l2):
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next
            p = p.next
        
        if l1:
            p.next = l1
        else:
            p.next = l2
        return newhead.next

