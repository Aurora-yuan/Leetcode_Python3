#label: link difficulty: medium

"""
思路：

emmm，第一眼看过去，这不是133吗。

本题是133变种题，区别在于133是图有邻居，138是链表有随机指针。

开一个哈希表mapping，key是老结点，val是新节点，

然后把 老结点（key）的next和random对应的新节点（mapping[key.next] 和mapping[key.random]） 

分别赋给新节点(val)的next （val.next）和random （val.random）。

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #133变种题， 图换成链表
        mapping = dict()
        
        p = head
        while p:
            mapping[p] = Node(p.val, None, None)
            p = p.next
            
        for key, val in mapping.items(): #key是老结点， val是新节点
            if key.next:
                val.next = mapping[key.next]
            if key.random and key.random in mapping:
                val.random = mapping[key.random]
            
        return mapping[head] if head else head


