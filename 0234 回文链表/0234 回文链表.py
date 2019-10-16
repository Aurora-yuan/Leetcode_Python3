#label: 双指针 difficulty: easy

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        l = []
        p = head
        while p.next:
            l.append(p.val)
            p = p.next
        l.append(p.val)
        return l == l[::-1]
        
  """
  上述解法空间占用太大。另一种解法空间复杂度O(1)，那么可以设置快慢指针，当快指针走完时，慢指针刚好走到中点，随即原地将后半段反转。然后进行回文判断。
  """
  
  # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        if head.next.next is None:
            return head.val == head.next.val
        fast = slow = q = head
        while fast.next and fast.next.next:#这里快指针的判读条件跟判断环形有一点不同
            fast = fast.next.next
            slow = slow.next
        def reverse_list(head):
            if head is None:
                return head
            cur = head
            pre = None
            nxt = cur.next
            while nxt:
                cur.next = pre
                pre = cur
                cur = nxt
                nxt = nxt.next
            cur.next = pre
            return cur
        p = reverse_list(slow.next)
        while p.next:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return p.val == q.val
