#label: tree difficulty: medium

"""
思路：

本题类似最近亚麻的OA题，零件合并:

https://www.1point3acres.com/bbs/forum.php?mod=attachment&aid=Mjk4NzE1fDA1YzQ2MmQ4Nzc4ZGI0YmU4NTlhYzA0MjI5MDk2NWYxfDE1NjM3MjU3MTc%3D&request=yes&_f=.png,

区别在于，亚麻的面试题里合并的开销是两者之和，

而本题合并的开销是两者之积。

根据贪心的思想，越大的数字用来合并的次数应该越少，这样才能实现题目中求最小值的要求。

因此，我们每次应当考虑，把数组里当前的最小值和它左右较小的那个值进行合并，(考虑最小值相邻的左右两个数是因为要满足树的中序遍历的顺序关系)

合并完成后，把这两个数的乘积加到答案里，然后把最小值删去不再考虑，

当数组中只剩下一个数字时候，就可以结束循环，

注意判断左右邻居不存在的边界情况。

"""


class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        while len(arr) > 1:
            min_val = min(arr)
            idx = arr.index(min_val)
            if idx > 0 and idx < len(arr) - 1: #有左有右
                left_val, right_val = arr[idx - 1], arr[idx + 1]
            elif idx == len(arr) - 1: #有左没右
                left_val, right_val = arr[idx - 1], 16 #为什么是16？因为最大只有15
            elif idx == 0: #有右没左
                left_val, right_val = 16, arr[idx + 1]
                
            res += min(min_val * left_val, min_val * right_val)
            arr.remove(min_val) #把当前最小值删掉，已经用完了
        return res

