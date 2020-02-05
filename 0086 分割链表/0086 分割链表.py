#label: 链表 difficulty: medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        pre = ListNode(-1)
        pre.next = head
        p = pre
        while p.next and p.next.val < x:
            p = p.next
        q = p.next
        r = q
        while r and r.next:
            if r.next.val >= x:
                r=r.next
            else:
                s = r.next
                r.next = r.next.next
                p.next = s
                s.next = q
                p = p.next
        return pre.next


        
