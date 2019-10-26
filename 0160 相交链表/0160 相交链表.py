#label: 链表 difficulty: easy

"""
第一种思路：

先分别找出两个链表的长度la, lb, 这样就可以知道二者长度的差值la - lb

然后让较长的那个链表先走la - lb步，

然后两个链表一起每次走一步，

第一次相遇的那个节点就是交点。

时间复杂度O(M + N)

"""

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa, pb = headA, headB
        la, lb = 0, 0
        while pa:
            la += 1
            pa = pa.next
        
        while pb:
            lb += 1
            pb = pb.next
            
        if la < lb:
            la, lb, headA, headB = lb, la, headB, headA
            
        n = la - lb
        pa, pb = headA, headB
        while n:
            pa = pa.next
            n -= 1
            
        while pa:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
        return None
“”“
第二种思路：

把链表A里的每个节点都记录在哈希表里，然后遍历链表B，返回第一个出现在哈希表里的节点。

时间复杂度O(M + N)，空间复杂度O(M)

”“”

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dic = {}
        p = headA
        while p:
            dic[p] = 1
            p = p.next
        p = headB
        while p:
            if p in dic:
                return p
            p = p.next
        return None

“”“
第三种思路:

把链表A里的每一个节点都在链表B里查找，时间复杂度O(MN)，空间复杂度O(1)
“”“


