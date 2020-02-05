#label: 双指针 difficulty: medium

"""
思路：

快慢指针法，快指针先走n步，然后快慢指针一起走，

当快指针是链表尾部的最后一个元素时，

慢指针指向元素的下一个元素就是需要删的那个元素。

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        slow,fast = head,head
        while n:
            n -= 1
            fast = fast.next
            
        if fast is None:
            return p.next
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return p
