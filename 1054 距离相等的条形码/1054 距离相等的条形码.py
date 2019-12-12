#label: heap difficulty: medium

"""
思路：

思路：

按照贪心的思想，首先放出现次数最多的元素在第一个，然后再把出现次数第二多的元素放第二个……

注意每放一个元素下去，它的频率就会 - 1，所以是一个动态的找出现频率最高元素的过程，

因此应该用Priority Queue来解题。

维护一个优先级队列，优先级是每个元素当前的频率，

每次把把队列最优先的元素POP出来，再插入到答案里，把它的频率 - 1，

为了避免相邻元素重复，先用pre把它先暂时保存在堆外，

插入下一个元素后，再把pre里保存的元素重新入堆。

"""

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        from collections import Counter
        import heapq
        
        record = Counter(barcodes) #统计每个数字出现的频率
        
        queue = []
        for key, val in record.items():
            queue.append([-val, key])
            
        heapq.heapify(queue) #建立优先级队列(堆)
 
        res = []
        pre = None
        while queue or pre:
            if queue:
                cur = heapq.heappop(queue) #取出当前出现次数最多的元素，如果次数相同则先进先出
                #frequency, value = cur[0], cur[1]
                res.append(cur[1]) #把它放到答案里
                cur[0] += 1 #给它的频率 - 1，因为Python仅支持最小堆，为了达到最大堆的效果，所以取了相反数操作
                if cur[0] == 0: #这个元素已经放好了
                    cur = None
            else:
                cur = None
            if pre: #把前一个插入的数再进行入堆操作
                heapq.heappush(queue, pre)
            pre = cur #把这一轮的数用pre保存起来，此时这个数不在堆里，可以保障相邻元素不会重复
                
        return res



