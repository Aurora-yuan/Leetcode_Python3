#label: dictionary difficulty: easy

class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        sums, count = 0, 0
        
        for each in S:
            sums += widths[ord(each) - 97]
            if sums > 100:
                count += 1
                sums = widths[ord(each) - 97]
        if sums:
            count += 1
        
        return [count, sums]


