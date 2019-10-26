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


