#label: heap difficulty: medium

class Solution:
    def reorganizeString(self, S: str) -> str:
        alpha_count = {}  # 贪心算法，先按字母频率排序，再不停取和上一个不重复的最大频率的即可
        for s in S:
            alpha_count[s] = alpha_count.get(s, 0) + 1
        if max(alpha_count.values()) > (len(S)+1)//2:
            return ''
        heap, res = [(-c, a) for a, c in alpha_count.items()], ' '
        heapq.heapify(heap)
        while heap:
            count, alpha = heapq.heappop(heap)
            if res[-1] == alpha:  # 重复
                temp = (count, alpha)  # 先把这一个缓存起来
                count, alpha = heapq.heappop(heap)  # 取下一个
                res += alpha
                heapq.heappush(heap, temp)  # 再把缓存的放回堆
            else:
                res += alpha
            if count < -1:  # 如果当前用掉的字母还剩，放回堆
                heapq.heappush(heap, (count+1, alpha))
        return res[1:]

