#label: string difficulty: easy

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        # 三种情况
        # 1、 两个字符串长度不相等，必然错误
        # 2、 两个字符串完全一致，需要至少有一个字母存在大于等于两次
        # 3、 两个字符串恰好只有两个位置不一样（只发生了一次交换）
        if A == B:
            if len(A) == len(set(A)):
                return False
            else:
                return True
        if len(A) != len(B):
            return False
        count = [] 
        for i in range(len(A)):
            if A[i] != B[i]:
                count.append(i)
        if len(count) != 2:
            return False
        if A[count[0]] == B[count[1]] and A[count[1]] == B[count[0]]:
            return True
        else:
            return False


