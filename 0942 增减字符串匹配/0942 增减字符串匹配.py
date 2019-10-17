#label: 贪心 difficulty: easy

"""

思路：

贪心一下，每次如果是I，就把当前最小的元素放到res里，这样下一个元素必然比当前元素大，保证了increase，

                  同理，如果是D，就把最大的放到res里，

最后记得处理最后一个元素，因为ID字符串的长度只有N，但是生成的数组长度有N+1

"""

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        left = 0
        right = len(S)
        res = []
        for char in S:
            if char == 'I':
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1
        res.append(right)
        return res
