#label: stack difficulty: medium

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n
        for log in logs:
            f, s, t = log.split(':')
            f, t = int(f), int(t)
            if s == "end":
                p = stack.pop()
                v = t - p[1] + 1
                res[f] += v
                if stack:
                    # 减去当前函数的执行时间，使用栈顶id的进行修改, 即外层函数的执行时间
                    #相当于栈顶id包含了该pop的id
                    res[stack[-1][0]] -= v
            else:
                stack.append((f, t))
        return res


