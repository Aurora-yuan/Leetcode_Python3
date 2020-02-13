#label: linknode difficulty: medium

"""
第一种思路：

暴力解，先把所有的值放在一个数组里，然后对数组排序，

再把数组里的值按顺序放到新的链表里。

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nums = []
        for i in range(len(lists)):
            while lists[i]:
                nums.append(lists[i].val)
                lists[i] = lists[i].next
                
        nums.sort()
        
        dummy = ListNode(1)
        p = dummy
        # print nums
        for i, num in enumerate(nums):
            p.next = ListNode(num)
            p = p.next
            
        return dummy.next

"""
第二种思路：

逐个调用LeetCode-Python-21. 合并两个有序链表里的合并两个链表的函数。

"""

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while len(lists) > 1:
            a = lists.pop() if len(lists) > 0 else None
            b = lists.pop() if len(lists) > 0 else None
            lists.insert(0, self.mergeTwoLists(a, b)) # 用append会超时
 
        return None if len(lists) < 1 else lists[0]
        
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newhead = ListNode(0)
        p = newhead
        while(l1 and l2):
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next
            p = p.next
        
        if l1:
            p.next = l1
        else:
            p.next = l2
        return newhead.next

"""
第三种思路：

利用一个size为K的优先级队列，

每次把K个链表的当前头的val塞进优先级队列，取pop出来的值作为结果链表的val。

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import *

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(pq,(lists[i].val,i))
                lists[i] = lists[i].next
                
        dummy = ListNode(-1)
        p = dummy
        while pq:
            val,idx = heappop(pq)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heappush(pq,(lists[idx].val,idx))
                lists[idx] = lists[idx].next
        return dummy.next
