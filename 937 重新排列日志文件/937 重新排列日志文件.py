#label: string difficulty: easy

"""
解题思路

首先想到的解法就是现将标识符后面是字母和数字的两种情况拆解开。
"""
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        digit_logs, letter_logs = list(), list()
        for log in logs:
            tmp = log.split(" ")
            if tmp[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        letter_logs.sort(key=lambda x:x.split(" ")[1:])
        return letter_logs + digit_logs

