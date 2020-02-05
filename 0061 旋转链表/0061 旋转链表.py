#label: 双指针 difficulty: medium

"""
第一种思路：

一般链表的题都有一种麻瓜解：先转List处理之后再转回链表。

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        p = head
        l = []
        while p:
            l.append(p.val)
            p = p.next
        if len(l) <= 1:
            return head
        if not k:
            return head
        k = k % len(l)
        l = l[-k:] + l[:-k]
        newhead = ListNode(-1)
        p = newhead
        for item in l:
            p.next = ListNode(item)
            p = p.next
        return newhead.next
        
"""
第二种思路：

观察一下，发现旋转的本质就是：

1. 找到倒数第K个节点，把它变成新的头，

2. 把原来的尾的next指向原来的头

3. 把倒数第K + 1个节点的next置空

所以可以用双指针的办法找到SLOW作为倒数第K+1个节点， FAST作为最后一个节点。
 
"""
 
 
