#label: 字符串 difficulty: easy
"""
先把所有的交易记录用哈希表，按照每个人的名字分好类，

然后在每个人的名字下的交易里，找满足无效交易的两个条件：

1. 交易金额超过1000。

2. 有不同城市的一小时内的其他转账记录。

注意用set存答案，避免重复。
"""
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        recordByName = collections.defaultdict(list)
        for trans in transactions:
            name,time,amount,city = trans.split(",")
            recordByName[name].append([name,int(time),int(amount),city]) #将所有的记录转换成哈希表（字典），通过交易名称进行索引
        def convert(l): #这个函数的功能是把格式转成输出需要的格式
            return l[0] + "," + str(l[1]) + "," + str(l[2]) + "," + l[3]
        
        res = set()
        for name, rec in recordByName.items():
            curRec = sorted(rec, key = lambda x:x[1]) #按时间排好序
            
            for i in range(len(curRec)):
                if curRec[i][2] > 1000: # 交易金额超过1000， 说明无效
                    res.add(convert(curRec[i]))
 
                for j in range(i + 1, len(curRec)):                    
                    if abs(curRec[j][1] - curRec[i][1]) > 60: # 只在距离当前时刻60S内找
                        break
                    if curRec[j][3] != curRec[i][3]: #存在无效交易
                        res.add(convert(curRec[i]))
                        res.add(convert(curRec[j]))
        return res

