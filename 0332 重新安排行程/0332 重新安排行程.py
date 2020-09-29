#label: 回溯算法 difficulty: medium

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # https://leetcode-cn.com/problems/reconstruct-itinerary/solution/pythonhui-su-suan-fa-ji-bai-9523-by-yun-yi-hen/
        from collections import defaultdict
        ticket_dict = defaultdict(list)
        for item in tickets:
            ticket_dict[item[0]].append(item[1])

        path = ['JFK']
        def backtrack(cur_from):
            if len(path) == len(tickets) + 1: #结束条件
                return True
            ticket_dict[cur_from].sort()
            for _ in ticket_dict[cur_from]:
                cur_to = ticket_dict[cur_from].pop(0)
                path.append(cur_to)
                if backtrack(cur_to):
                    return True
                path.pop()
                ticket_dict[cur_from].append(cur_to)

            return False

        backtrack('JFK')
        return path
