#label: string difficulty: medium


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = dict()
        
        for word in strs:
            tmp = tuple(sorted(word))
            # print tmp
            if tmp in list(record.keys()):
                record[tmp].append(word)
            else:
                record[tmp] = [word]
        return [val for key, val in record.items()]


