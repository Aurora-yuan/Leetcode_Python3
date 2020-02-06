#label: link difficulty: medium

"""
思路：

递归

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: #0个或者1个元素不用去重
            return head            
        newhead = ListNode(-1) #设置dummyhead
        newhead.next = head
        if head.val != head.next.val: #如果前两个节点不同，说明第一个节点一定有效
            head.next = self.deleteDuplicates(head.next)
        else:           #如果前两个节点相同，就一直往后找，直到找到链表结束或者找到跟头节点值不同的节点p
            p = head
            while p and p.val == head.val:
                p = p.next
            newhead.next = self.deleteDuplicates(p)
            
        return newhead.next


“”“
麻瓜思路：

转list，去重，转链表。

”“”

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        l = []
        p = head
        while p: #转list
            l.append(p.val)
            p = p.next
            
        i = 0
        ll = []#不含重复元素的list
        while i < len(l):
            if i + 1 < len(l):
                if l[i] != l[i + 1]: #不重复
                    ll.append(l[i])
                else: #重复了
                    tmp = l[i]
                    j = i + 1
                    while j < len(l) and l[j] == tmp:
                        j += 1
                    i = j #j是下一个元素的下标
                    continue
            else: #最后一个元素单独考虑
                if i != 0 and l[i] != l[i - 1]: 
                    ll.append(l[i])
            i += 1
            
        newhead = ListNode(-1)
        p = newhead
        for num in ll:
            p.next = ListNode(num)
            p = p.next
            
        return newhead.next
            



