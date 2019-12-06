#label: tree difficulty: medium

"""
对于一个简单的树

  4
 / \
#   # 

有一个非空节点可两个空节点

如果加上一个非空节点，同时也会多出一个空节点

   4   
  / \  
#   1 
   / \   
  #   # 

也就是说每加上一个非空节点，都会多出一个空节点

即空节点的数量=非空节点数量+1

如果不相等的话return false

因为字符串是前序遍历，所以一定是后遍历子节点

对于任意位置i，如果前i个字母中#的数量比数字数量+1多的话，便return false（t个非空节点只能有t+1个空节点做子节点，多余的空节点没地方放）

"""

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        #空节点的数量=非空节点数量+1
        t=1
        l=preorder.split(',')
        for i in l:
            if t==0:return False
            if i == "#":
                t=t-1
            else:
                t=t+1
        return t==0

