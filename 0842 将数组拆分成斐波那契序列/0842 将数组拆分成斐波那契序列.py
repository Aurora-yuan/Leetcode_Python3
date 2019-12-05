#label: 暴力解法 difficulty: medium

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        for i in range(min(10, len(S))):
            x = S[:i+1]
            if x != '0' and x.startswith('0'): break
            a = int(x)
            for j in range(i+1, min(i+10, len(S))):
                y = S[i+1: j+1]
                if y != '0' and y.startswith('0'): break
                b = int(y)
                fib = [a, b]
                k = j + 1
                while k < len(S):
                    nxt = fib[-1] + fib[-2]
                    nxtS = str(nxt)
                    if nxt <= 2**31 - 1 and S[k:].startswith(nxtS):
                        k += len(nxtS)
                        fib.append(nxt)
                    else:
                        break
                else: #在 python 中，while … else 在循环条件为 false 时执行 else 语句块：
                    if len(fib) >= 3:
                        return fib
        return []
