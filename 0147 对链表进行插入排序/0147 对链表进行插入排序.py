#label: link/sort difficulty: medium

"""
思路：

新建链表，把输入链表的每一个节点依次插入到新链表对应的位置。

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1)
       
        cur = head
        while cur:
            tail = cur.next
            p = dummy
            while p.next and p.next.val < cur.val:
                p = p.next
                
            cur.next = p.next 
            p.next = cur
            cur = tail
            
        return dummy.next




