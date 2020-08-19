# label: link difficulty: medium

"""
思路一：

麻瓜解，把链表转成list，再用list 生成结果链表。

转成list 的过程可以用dfs，也可以把输入看做二叉树，利用先序遍历得到list。

时间复杂度：O（N）

空间复杂度：O（N）

"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        self.l = []
        def inorder(node):
            if not node:
                return
            self.l.append(node.val)
            inorder(node.child)
            inorder(node.next)
        
        inorder(head)
        newhead = Node(self.l[0], None, None, None)
        pre = newhead
        for i in range(1, len(self.l)):
            cur = Node(self.l[i], pre, None, None)
            pre.next = cur
            pre = cur
        return newhead

“”“
思路二：

利用栈的迭代解。

时间复杂度：O（N）

空间复杂度：O（N）
“”“

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        stack = []
        node = head
        while node:
            if node.child:
                if node.next: # 如果存在 next 部分
                    stack.append(node.next) # 就保存
                node.child.prev = node # 让 node.child 变成 node.next
                node.next = node.child # 同上
                node.child = None # 置空 node.child
            if not node.next and stack: # 如果走到底没有next了，就把之前保存的 next 拿出来
                last_next = stack.pop() # stack里最后一个就是最新的 next
                node.next = last_next # 让它，变成当前 node 的 next
                last_next.prev = node
                
            node = node.next
        return head

