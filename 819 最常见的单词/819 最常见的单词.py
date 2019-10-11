#label: string difficulty: easy

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        tokens = re.sub('[\!\?\'\,\;\.]',' ',paragraph.lower()).split()
        cnt = collections.Counter(tokens)
        for ban in banned:
            if ban in cnt:
                del cnt[ban]
        return cnt.most_common(1)[0][0]
