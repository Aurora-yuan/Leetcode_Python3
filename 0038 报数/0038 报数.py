#label: string difficulty: easy

class Solution:
    def countAndSay(self, n: int) -> str:
        record = ["1"]
        for i in range(1,n):
            tmp= ""
            idx = 0
            pre = record[i-1]
            while idx < len(pre):
                cnt = 1
                while idx+1<len(pre) and pre[idx] == pre[idx+1]:
                    cnt += 1
                    idx += 1
                tmp += str(cnt) + pre[idx]
                idx += 1
            idx += 1
            record.append(tmp)
        return record[-1]
            
