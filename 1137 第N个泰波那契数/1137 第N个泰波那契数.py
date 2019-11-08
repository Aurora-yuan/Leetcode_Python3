#label: recursive difficulty: easy

class Solution:
    def tribonacci(self, n: int) -> int:
        # t0,t1,t2 = 0,1,1
        # return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        res = [0, 1, 1, 2]
        if n <= 2:
            return res[n]
        cnt = 2
        while cnt < n - 1:
            res[0] = res[1]
            res[1] = res[2]
            res[2] = res[3]
            res[3] = res[0] + res[1] + res[2]
            cnt += 1
            # print res, cnt
        return res[-1]


