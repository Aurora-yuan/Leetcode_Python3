#label: 二分查找/双指针 difficulty: easy

"""
双指针对碰法，设置两个指针left和right分别指向数组头和尾，

如果对应的值的和小于target， 说明目前left指向的元素太小了，跟最大的加在一起都达不到target的要求，所以它肯定不是答案，left后移一位，

同理，如果对应的值的和大于target，说明目前right指向的元素太大了，right前移一位。

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      
        left, right = 0, len(numbers) - 1
        while 1:
            tmp = numbers[left] + numbers[right]
            if tmp == target:
                return [left + 1, right + 1]
            elif tmp < target:
                left += 1
            elif tmp > target:
                right -= 1
