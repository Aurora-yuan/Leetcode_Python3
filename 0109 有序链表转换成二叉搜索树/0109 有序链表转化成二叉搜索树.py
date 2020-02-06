#label: link difficulty: medium

"""
思路：

用快慢指针找到链表的中点，然后递归建树。

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow,fast = head,head
        pre = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        part1 = head
        part2 = slow.next
        
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(part1)
        root.right = self.sortedListToBST(part2)
        
        return root
