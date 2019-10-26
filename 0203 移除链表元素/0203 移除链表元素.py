#labels: 链表 difficulty: easy

"""
思路：

双指针法，pre和cur分别指着当前节点的前一个节点，和当前节点，

然后按删除node的流程操作就可以。

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre,cur = dummy,head
        while cur:
            if cur.val == val:
                pre.next = cur.next
                cur.next = None
                cur = pre.next
            else:
                pre = pre.next
                cur = cur.next
        return dummy.next
