#label: 链表 difficulty: easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        res = {}
        while head != None:
            count += 1
            res[count] = head
            head = head.next
        #j = math.ceil(count/2)
        #if count % 2 == 0:
        #    return res[j+1]
        #else:
        #    return res[j]
        j = math.ceil((count-1)/2) + 1
        return res[j]

