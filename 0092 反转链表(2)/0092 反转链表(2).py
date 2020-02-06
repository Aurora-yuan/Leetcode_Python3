#label: link difficulty: medium

"""
思路：

先找到m ~ n 这一段，然后记录两个关键的节点：

1. m的前一个节点pre_m

2. n的后一个节点nextn

然后把m 到 n翻转，再让pre_m的next指向翻转的结果， 再让翻转结果的末尾指向nextn

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 先找到m ~ n这一段，翻转，再塞回去
        if m == n:
            return head
        cnt = 1
        pre_m, pn = None, None # pre_m代表m的前节点，pn代表n这个节点
        node = head
        while(cnt < n):
            if cnt == m - 1:
                pre_m = node
            node, cnt = node.next, cnt + 1
        pn = node
        if pn:
            nextn = pn.next
            pn.next = None
        else:
            nextn = None
         
        if pre_m is None: #从1开始
            head = self.reverseList(head)
            newhead = head
            while(head.next):
                head = head.next
            head.next = nextn
            return newhead
        else:
            pre_m.next = self.reverseList(pre_m.next)
            newhead = head
            while(head.next):
                head = head.next
            head.next = nextn
            return newhead
        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        tmp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tmp




