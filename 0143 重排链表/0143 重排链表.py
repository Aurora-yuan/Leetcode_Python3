#label: link difficulty: medium

"""
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        slow, fast = head, head
        while fast and fast.next: #快慢指针找中点
            slow = slow.next
            fast = fast.next.next
        
        l1, l2 = head, self.reverseList(slow.next) #把后半段链表翻转
        slow.next = None #前半段的末尾记得置空
        while l1 and l2:
            cur = l2 #每次把后半段链表的第一个拿出来
            l2 = l2.next
 
            cur.next = l1.next #插到前半段链表里
            l1.next = cur
            l1 = l1.next.next 
 
        return head
    
    def reverseList(self, head):
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
    

